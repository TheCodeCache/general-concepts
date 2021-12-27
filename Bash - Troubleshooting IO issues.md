# Troubleshooting I/O performance issues on Linux - 

When we run `find` command or `copy` command or just observing few things are extremely slow,  
or we've an application running on the linux machine which seems to be very slow, then we need to identify the bottleneck.  

**Step-1:**  
let's find how many disk devices we;ve on the linux machine: 

![image](https://user-images.githubusercontent.com/26399543/147406141-395bc340-2215-4d62-b21c-d74acc4b21c5.png)

In the above, there're 2 disks and each disk has got one 8GB partitions.  

**Step-2:**  
let's run `top` command, this cmd gives us a fairly good idea about the general resource usage on the machine.  

![image](https://user-images.githubusercontent.com/26399543/147406224-bcafadd9-d331-4fbc-b287-498bc1b6b0fd.png)

In the above image, we can observe that the CPU usage is normal, it seems to be stable under 20-25 %  
However, the `wa` (%) does not seem to be normal, it is in range 65-85 % and if this wait (%) is > 20 % then, in general, it usually becomes a concern  

wa(%) - the amount of time CPU is spending waiting for I/O operations to finish.  

So, we've confirmed that the bottleneck in our case, is actually I/O performance.  

**Step-3:**  
let's pinpoint exactly which of those 2 disks are experiencing I/O performance issues.  
and the best way to do this is to use `iostat` command  

![image](https://user-images.githubusercontent.com/26399543/147406334-ce3fefc2-3d8d-4640-9526-ff56679ae885.png)

Based on the above outcomes, we can be sure that it's disk-2 (xvdf) that is suffering from I/O issues.  

**Step-4:**  
Let's us now find out what is the process or the job or the application that is hogging all of I/O resouces of that disk  
so, the way we can do this is to use a command called `iotop` and this command is usually not installed by default on all linux machines,  
so, let us install it if it is not installed like below:  
`yum -y install iotop`  

let us run `iotop -o` option, we'd get the following output - 
we use `-o` option displays only those processed that actually do I/O activity and ignores others.  

![image](https://user-images.githubusercontent.com/26399543/147406460-30b90cce-2524-4325-b4ba-1d85e789dad3.png)

so, we've got only few processes that're doing I/O one of which is a kernel worker (which can be ignored as this is not the user process)  
so, if we observe the first 2 processes are hogging all of I/O on our disk  

This's how we troubleshoot I/O issues on Linux machines  

**Note:**  
We can use `iostat`, `vmstat`, and `sar` commands to check disk I/O performance.  
We can also check disk read and write activity by process using the `iotop` command.

**Reference:**  
1. https://www.youtube.com/watch?v=sjyLRS52zOg
2. https://www.baeldung.com/linux/monitor-disk-io

