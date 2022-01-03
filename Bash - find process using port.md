
# multiple process binding to same port — 

It's possible to have multiple process running at a given port, using `SO_REUSEPORT` option:  

The basic concept of SO_REUSEPORT is simple enough.  
Multiple servers (processes or threads) can bind to the same port if they each set the option as follows:  

```shell
int sfd = socket(domain, socktype, 0);

int optval = 1;
setsockopt(sfd, SOL_SOCKET, SO_REUSEPORT, &optval, sizeof(optval));

bind(sfd, (struct sockaddr *) &addr, addrlen);
```

# find all process listening at a given port — 

Following are the methods using which we could find the `PID` of the Process Using a Specific `Port`:  


**Note:** we should use `sudo` to run the below commands as follows,  
in order to get the PID and process name listening on a port  


1. using `netstat`:  

```shell
ubuntu@ip-172-31-42-44:~$ sudo apt install net-tools
ubuntu@ip-172-31-42-44:~$ sudo netstat -ltnup | grep ':80'
tcp6       0      0 :::80                   :::*                    LISTEN      505/apache2
```

In the above example:  we first installed `net-tools`  
which will give us `netstat` cmd using which we've identified the process running on port 80, which is apache2  

2. using `lsof`:  

```shell
ubuntu@ip-172-31-42-44:~/flask$ sudo lsof -i :80
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1089     root    7u  IPv4  27098      0t0  TCP *:http (LISTEN)
nginx   1089     root    8u  IPv6  27099      0t0  TCP *:http (LISTEN)
nginx   1090 www-data    7u  IPv4  27098      0t0  TCP *:http (LISTEN)
nginx   1090 www-data    8u  IPv6  27099      0t0  TCP *:http (LISTEN)

ubuntu@ip-172-31-42-44:~/flask$ sudo lsof -i :443
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1089     root    9u  IPv4  27100      0t0  TCP *:https (LISTEN)
nginx   1090 www-data    9u  IPv4  27100      0t0  TCP *:https (LISTEN)
```
we can use below to search for multiple ports at once:  
```
ubuntu@ip-172-31-42-44:~/flask$ sudo lsof -i :80 -i :443
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1089     root    7u  IPv4  27098      0t0  TCP *:http (LISTEN)
nginx   1089     root    8u  IPv6  27099      0t0  TCP *:http (LISTEN)
nginx   1089     root    9u  IPv4  27100      0t0  TCP *:https (LISTEN)
nginx   1090 www-data    7u  IPv4  27098      0t0  TCP *:http (LISTEN)
nginx   1090 www-data    8u  IPv6  27099      0t0  TCP *:http (LISTEN)
nginx   1090 www-data    9u  IPv4  27100      0t0  TCP *:https (LISTEN)
```

3. using `ss`:  

```shell
ubuntu@ip-172-31-42-44:~/flask$ sudo ss -ltnup 'sport = :80'
Netid  State   Recv-Q   Send-Q     Local Address:Port     Peer Address:Port  Process
tcp    LISTEN  0        511              0.0.0.0:80            0.0.0.0:*      users:(("nginx",pid=1090,fd=7),("nginx",pid=1089,fd=7))
tcp    LISTEN  0        511                 [::]:80               [::]:*      users:(("nginx",pid=1090,fd=8),("nginx",pid=1089,fd=8))

ubuntu@ip-172-31-42-44:~/flask$ sudo ss -ltnup 'sport = :443'
Netid        State         Recv-Q        Send-Q               Local Address:Port               Peer Address:Port        Process
tcp          LISTEN        0             511                        0.0.0.0:443                     0.0.0.0:*            users:(("nginx",pid=1090,fd=9),("nginx",pid=1089,fd=9))
```



**Reference**:  
1. https://lwn.net/Articles/542629/

