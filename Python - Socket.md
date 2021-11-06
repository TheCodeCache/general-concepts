About Socket-  
. . .   
.  
.  
.  
IPC: (stands for Inter Process Communication)  
  IPC  
  If you need fast IPC between two processes on one machine, you should look into pipes or shared memory.   
  If you do decide to use AF_INET sockets, bind the “server” socket to 'localhost'.   
  On most platforms, this will take a shortcut around a couple of layers of network code and be quite a bit faster.  
  
  The multiprocessing integrates cross-platform IPC into a higher-level API.  
    https://docs.python.org/3/library/multiprocessing.html#connection-objects  
      class multiprocessing.connection.Connection  
  
  
  
Reference:  
  https://docs.python.org/3/howto/sockets.html  
   
