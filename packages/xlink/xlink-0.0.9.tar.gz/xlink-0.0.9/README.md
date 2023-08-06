# xlink
Master与Slave心跳协议说明：
  Master与Slave之间通过multiprocessing的BaseManager进行通讯
  Master需要先启动，Slave后启动，Slave（在整个生命周期）启动时先调用且只调用一次bind方法与Master绑定
  Slave定时（秒级）通过take方法获取Master的分法信息（schedule key）
  Slave在take的时候也会（上）传自己的指标作为参数给Master接收
  如果Master超时（分钟级）没有接收Slave的take请求，则判断Slave已失联，废弃该Slave，Slave同事也会在分钟级内自行关闭