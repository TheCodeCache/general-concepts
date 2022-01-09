# Non-Blocking I/O — 

An extremely-fast servers has 2 characteristics as follows:  

1.  Accept and Respond to as many connections as they can
2.  Respond quickly to client requests

To achieve the above goals, we've below options:  
1. Threads (good for low RPS/CPS i.e. Request/Connection Per Second)
2. Processes (not recommended)
3. Non-Blocking I/O (best)
4. Busy-wait (worst)

We should almost always avoid busy-wait, in general, as it consumes nearly all of the available CPU.  

# Non-blocking IO under the hood — 

Most `non-blocking frameworks use an infinite loop that constantly checks (polls) if data is returned from IO`.  
This is often called the `event loop`. An event loop is literally a `while(true)` loop  
that in each iteration will check if data is ready to read from a network socket.  
Technically, sockets are implemented as file descriptors (FD) on UNIX systems.  

We might think that an `event loop` can be expensive on the CPU if it's endlessly running,  
but there are some optimizations to make them more efficient.  

Let’s zoom a bit in on the event loop to see how these optimizations work.  
Each (major) operating system provides kernel level APIs support to help create an event loop.  
In Linux there is `epoll` or io_uring, BSD uses `kqueue` and Windows has `IOCP`.  
Each of these APIs is able to check FDs for ready data with a computational complexity of around `O(number_of_events_occurred)`.  
In other words, you can monitor 100.000s of FDs,  
but the API's execution speed only depends on the amount of events that occur in the current iteration of the event loop.  
Compared to the older poll and select APIs this is a huge improvement:  

![image](https://user-images.githubusercontent.com/26399543/148661743-18b81a50-5001-4a78-9b6e-6f5e3c0c7884.png)  

`epoll` scales (linearly) according to the number of I/O events that occur.  
The epoll API is thus particularly efficient in a scenario that is common in  
servers that handle many simultaneous clients: of the many file descriptors being  
monitored, most are idle; only a few descriptors are ready  

`epoll()` system-call is a way to achieve `non-blocking i/o` in Linux  

High-performance web servers like `nginx` uses `epoll()` system-call to handle millions of requests/connections per second  

![image](https://user-images.githubusercontent.com/26399543/148698354-43253acf-9586-42d0-b7dc-7032d6d933e6.png)  


**Reference:**  
1. https://medium.com/ing-blog/how-does-non-blocking-io-work-under-the-hood-6299d2953c74
2. https://www.youtube.com/watch?v=y5xvYX0m61E
3. https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/

