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

![image](https://user-images.githubusercontent.com/26399543/147362859-9b1f6443-aaca-4f2d-a344-793eb8f57224.png)

Similarly, we can also send something from the server process to the client process  

![image](https://user-images.githubusercontent.com/26399543/147362909-af4491b7-5c94-40fc-9aaf-18ee7c5bb065.png)

# Setting up a minimal server - 
It’s also possible to run a web server using netcat that returns data whenever a client connects to the server.  

Let’s first create an index.html file that the server will serve to any connecting clients:  
```html
cat - > index.html <<<EOF
<!DOCTYPE html>
<html>
    <head>
        <title>Simple Netcat Server</title>
    </head>
    <body>
        <h1>Welcome to simple netcat server!<h1>
    </body>
    </body>
<html>
EOF
```
we’ll start a netcat process that listens to port 1234 and serves the file whenever a client connects to our server:  
```shell
$ echo -e "HTTP/1.1 200 OK\n\n$(cat index.html)" | nc -l 1234
```
The command above first constructs a legitimate HTTP response using echo and process substitution.  
Then, we pipe the response to the netcat process that is listening on port 1234.  

Let’s open up our browser and visit localhost:1234.  

![image](https://user-images.githubusercontent.com/26399543/147363141-a5200e9d-93ec-49e4-ab06-c0118a42bb58.png)

# Improving the Server - 
There are two issues with the server we’ve implemented:  

1. The connection doesn’t terminate even when the data transfer is complete
2. The server only serves a single client
these 2 issues would be fixed using the below enhanced script:  
```shell
$ while true; do echo -e "HTTP/1.1 200 OK\n\n$(cat index.html)" | nc -l -w 1 1234; done
```
First, using the -w flag allows us to specify the timeout value  
Second,we wrapped the command into a while loop. In consequence, whenever the command terminates, it’ll restart the process

whenever a client is connected to the server, the netcat process returns the HTTP response.  
After one second of idle, the process terminates and returns.  
Finally, the while loop will then restart the process, starting the netcat process once again listening on port 1234  

