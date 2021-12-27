
Use `free` command to view `Buffer` and `Cache` Usage.  

![image](https://user-images.githubusercontent.com/26399543/147459065-0fd07b97-043c-4ca7-831f-95919cb817e5.png)

there is 7.5 GB of total RAM. Of this, only 209 MB is in use, and 6.5 GB is free. `Buffer` and `cache` are using this 667 MB  

Now, let's try to increase that number by running a command to generate and read a file of 1 GB:  

```shell
# dd if=/dev/random of=/root/data_file count=1400000
# for i in `seq 1 10`; do echo $i; cat data_file >> large_file; done
```

Now, we'll make sure to read this 1 GB file and check the usage with the free command again:  

```shell
# cat large_file > /dev/null; free -m

             total        used        free      shared  buff/cache   available
Mem:          7457         206         5515          0        1735        6992
Swap:           0           0           0
```

We can see that the `buffer and cache` usage has gone up from 667 to 1735 MB, a roughly `1 GB` increase in its use.  

**Experimental Verification of How Cache Works**:  
Let’s do some performance validation to see how the kernel reads a file using the cache?  
Let’s read a file and write it back to /dev/null to test how long it takes to read the file from the disk using `time` command  

```shell
# ls -l                                                                                                                              
total 525448                                                                                                                                           
-rw-r--r-- 1 root root  49032472 Nov 20 09:13 data_file                                                                                                
-rw-r--r-- 1 root root 490324720 Nov 20 09:15 large_file
```
```shell
# time cat large_file >> /dev/null                                                                                                   
                                                                                                                                                       
real    0m4.478s                                                                                                                                       
user    0m0.004s                                                                                                                                       
sys     0m0.388s
```
It took 4.478 seconds to read the file. Let’s read it again. As the file is in the file system cache, it should take less time now (which is interesting):  
```shell
# time cat large_file >> /dev/null                                                                                                   
                                                                                                                                                   
real    0m0.602s                                                                                                                                       
user    0m0.002s                                                                                                                                       
sys     0m0.393s
```
It took only 0.602 seconds to read the file when it was cached.  

Hence, it is quite evident that the use of `buffer and cache` makes `I/O` operations faster.  

# How to Empty Buffer, Cache, and Swap - 

If we want to empty buffer and cache, we can use this chain of commands:  

```shell
free && sync && echo 3 > /proc/sys/vm/drop_caches && free
```

the above cmd is one way of dropping cache.  
There are three ways in which the Linux kernel drops cached items,  

use `echo 1` to free `page cache`:  
```shell
echo 1 > /proc/sys/vm/drop_caches
```
use `echo 2` to free `dentries and inodes`:  
```shell
echo 2 > /proc/sys/vm/drop_caches
```
use `echo 3` to free `page cache, dentries, and inodes`:  
```shell
echo 3 > /proc/sys/vm/drop_caches
```

# Command to Clear Out Swap**:  
we already know - Swap space temporarily holds data moved from the system RAM.  
In order to clean up swap space, we can disable and enable it like below.  

```shell
swapoff -a && swapon -a
```

**Reference**:  
1. https://www.baeldung.com/linux/empty-buffer-cache

