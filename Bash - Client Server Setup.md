# Simple Client-Server set up in Linux - 

**Notes about `netcat`:**  

We can use `netcat` command in Linux for this excercise in Linux.  
`netcat` is a powerful networking utility tool. Its purpose is reading and writing data across the network, through TCP or UDP.  
 
# Scanning for Open Ports Using `netcat` - 
 
Let’s scan for any open ports at google.com in the range of 442–444 ?
```shell
$ nc -z -v -w 1 google.com 442-444
nc: connect to google.com port 442 (tcp) timed out: Operation now in progress
nc: connect to google.com port 442 (tcp) failed: Cannot assign requested address
Connection to google.com 443 port [tcp/*] succeeded!
nc: connect to google.com port 444 (tcp) timed out: Operation now in progress
nc: connect to google.com port 444 (tcp) failed: Cannot assign requested address
```
The command will attempt to connect to google.com on port 442 to 444.  
From the output, we can see that port 443 is open as the connection attempt is successful.  
On the other hand, ports 442 and 444 aren’t open as the connection attempt timed out.  

# Client-Server Setup - 

As `netcat` allows both reading from and writing to network connections, we can build a simple client-server setup.  
To start our server, we need to open a terminal session and then start a 1netcat` server process  

```shell
$ nc -lv 1234
Listening on 0.0.0.0 1234
```
First, the `-l` flag instructs netcat to listen to the specified port, 1234. Then, the `-v` flag enables the verbose mode.  
Once executed, the process will listen indefinitely until it is killed.  

Now, let us open up a new terminal session to connect to the server process,  
```shell
$ nc -v localhost 1234
Connection to localhost 1234 [tcp/*] succeeded
```
Running that command will open up a netcat process that connects to localhost at port 1234.  
From the output, it shows that the connection is successfully established.  

Once we have both the client and server process running,  
let’s send some data between these two processes. In our client process, we can enter some text and press enter:  
