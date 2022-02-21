  
References:   
  https://serverfault.com/a/238534  
  https://blog.codinghorror.com/the-infinite-space-between-words/  
  http://highscalability.com/numbers-everyone-should-know
  
Numbers Everyone Should Know  
Operation|time  
---------|----  
L1 cache reference|0.5 ns  
Branch mispredict|5 ns  
L2 cache reference|7 ns  
Mutex lock/unlock|100 ns (25)  
Main memory reference|100 ns  
Compress 1K bytes with Zippy|10,000 ns (3,000)  
Send 2K bytes over 1 Gbps network|20,000 ns  
Read 1 MB sequentially from memory|250,000 ns  
Round trip within same datacenter|500,000 ns  
Disk seek|10,000,000 ns  
Read 1 MB sequentially from network|10,000,000 ns  
Read 1 MB sequentially from disk|30,000,000 ns (20,000,000)  
Send packet CA->Netherlands->CA|150,000,000 ns  
  
Do you have an I/O bottleneck?  
  Your I/O wait measurement is the canary for an I/O bottleneck. I/O Wait is the percentage of time your processors are waiting on the disk.  
  For example, let us say it takes 1 second to grab 10,000 rows from MySQL and perform some operations on those rows. The disk is being accessed while the rows are retrieved. During this time, the processor is idle. It is waiting on the disk.  
  In the example above, disk access took 700 ms, so I/O wait is 70%.  
  You can check your I/O wait percentage via top, a command available on every flavor of Linux:  
  If your I/O wait percentage is greater than (1/# of CPU cores) then your CPUs are waiting a significant amount of time for the disk subsystem to catch up.  
  In the output above, I/O wait is 12.1%. This server has 8 cores (via cat /proc/cpuinfo). This is very close to (1/8 cores = 0.125). Disk access may be slowing the application down if I/O wait is consistently around this threshold.  
  
What impacts I/O performance?  
  For random disk access (a database, mail server, file server, etc), you should focus on how many input/output operations can be performed per second (IOPS).  
  Four primary factors impact IOPS:  
    Multi-disk Arrays- More disks in the array mean greater IOPS. If one disk can perform 150 IOPS, two disks can perform 300 IOPS.  
    Average IOPS per-drive- The greater the number of IOPS each drive can handle, the greater the total IOPS capacity. This is largely determined by the rotational speed of the drive.  
    RAID Factor- Your application is likely using a RAID configuration for storage, which means you are using multiple disks for reliability and redundancy.  
    Read and Write Workload- If you have a high percentage of write operations and a RAID setup that performs many operations for each writes request (like RAID 5 or RAID 6); your IOPS will be significantly lower.  
  
Three takeaways  
  Disk access is slow- Disk access speeds do not come close to approaching RAM.  
  Optimize your apps first- Tuning your disk hardware is not trivial or likely to be a quick fix. Try to have your I/O-heavy services read more data from a RAM cache first.  
  Measure- Modifications to your application can have a big impact on Disk I/O. Record the key I/O metrics over time.  
  
  
