# Reverse Proxy with `netcat` - 

Let's assume there’s a service listening on port 4321. and however, external traffic can only access the host through port 1234.  
With `netcat`, we can set up a `reverse proxy` to redirect the traffic from port 1234 to port 4321, and vice versa.  

First, we’ll create a `named pipe`:  
```shell
$ mkfifo /tmp/rp
```
Then, we’ll create the `reverse proxy`:  
```shell
$ nc -lv 1234 < /tmp/rp | nc localhost 4321 > /tmp/rp
```
From the command, we've created two netcat processes.  
Let's call the first process the external router and the second process the internal router.  

When there is incoming traffic on port 1234, the external router pipes the traffic to the internal router.  
On the other hand, when there's outgoing traffic from port 4321, the internal router will pipe it to the named pipe /tmp/rp.  
Then, the external router will read and send the content of /tmp/rp to the client.  

Reference:  
1. https://www.baeldung.com/linux/netcat-command#reverse-proxy-with-netcat

