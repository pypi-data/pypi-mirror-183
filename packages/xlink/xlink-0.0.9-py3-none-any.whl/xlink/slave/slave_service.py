import sys
import time
import traceback
import threading
from queue import Queue
from .register_manager import RegisterManager
from .slave_client import SlaveClient
from loguru import logger


class ShouldReconnectException(Exception):

    pass


class SlaveService(threading.Thread):

    def __init__(self, host, port, authkey, receive_queue, batch_num=3000):
        assert type(receive_queue) is Queue
        threading.Thread.__init__(self)
        manager = RegisterManager(host, port, authkey)
        self._client = SlaveClient(manager)
        self._receive_queue = receive_queue
        self._checksum = 0
        self._batch_num = batch_num
        self._is_active = True
        self._heartbeat_time = 99999999999
        self._heartbeat_timeout = 3
        self.daemon = True

    # def __init__(self, client, receive_queue, batch_num=1000):
    #     assert type(receive_queue) is Queue
    #     self._client = client
    #     self._receive_queue = receive_queue
    #     self._checksum = 0
    #     self._batch_num = batch_num
    #     self._is_active = True
    #     self._heartbeat_time = 99999999999
    #     self._heartbeat_timeout = 3

    def is_connecting(self, now=None):
        if now is None:
            now = int(time.time())
        if now - self._heartbeat_time > self._heartbeat_timeout:
            return False
        return True

    def run_once(self):
        code, result = self._client.take(self._checksum, self._batch_num)
        if code not in [200, 300]:
            print(result)
            if code == 403:
                raise ShouldReconnectException('should reconnect!')
            return False
        if code == 300:
            logger.warning(f'checksum not match {self._checksum}!!!!')
        msg_list = result
        for msg in msg_list:
            self._receive_queue.put(msg)
            self._checksum += int.from_bytes(str.encode(msg), byteorder='little')
            print(f'my _checksum = {self._checksum}, len = {self._receive_queue.qsize()}')
        return len(msg_list)

    def run(self):
        assert self._is_active is True
        self._client.bind()
        while self._is_active:
            try:
                msg_len = self.run_once()
                self._heartbeat_time = int(time.time())
                if msg_len == 0:
                    time.sleep(2)
            except EOFError as e:
                logger.error(f'EOFError when request_with_unique_key: {e}')
                self.reconnect()
            except BrokenPipeError as e:
                # [Errno 32] Broken pipe
                logger.error(f'BrokenPipeError when request_with_unique_key: {e}')
                self.reconnect()
            except ConnectionResetError as e:
                # [Errno 54] Connection reset by peer
                logger.error(f'ConnectionResetError when request_with_unique_key: {e}')
                self.reconnect()
            except ConnectionAbortedError as e:
                logger.error(f'ConnectionAbortedError when request_with_unique_key: {e}')
            except ShouldReconnectException as e:
                logger.error(e)
                self.reconnect()
            except Exception as e:
                logger.error(f'{e}, {traceback.print_exc()}')
            finally:
                pass

    def reconnect(self):
        self._client.reconnect()
        self._checksum = 0
        self._receive_queue.queue.clear()
        self._client.bind()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 22222
    authkey = b'aaa'
    for _ in range(15):
        manager = RegisterManager(host, port, authkey)
        client = SlaveClient(manager)
        # client.bind()
        worker = SlaveService(client, 3000)
        thread = threading.Thread(target=worker.run, daemon=True)
        thread.start()
