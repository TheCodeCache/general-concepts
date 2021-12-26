# Create Memory Load on Linux machines - 

# using `stress-ng`

`stress-ng` is a workload generator that simulates cpu/mem/io/hdd stress on POSIX systems.  
This call should do the trick on Linux < 3.14:  

```shell
stress-ng --vm-bytes $(awk '/MemFree/{printf "%d\n", $2 * 0.9;}' < /proc/meminfo)k --vm-keep -m 1
```

For Linux >= 3.14, we may use MemAvailable instead to estimate available memory for new processes without swapping:  

```shell
stress-ng --vm-bytes $(awk '/MemAvailable/{printf "%d\n", $2 * 0.9;}' < /proc/meminfo)k --vm-keep -m 1
```

# using `malloc()`

We can write a C program to malloc() the required memory and then use mlock() to prevent the memory from being swapped out.  

Then just let the program wait for keyboard input, and unlock the memory, free the memory and exit.  


**Reference:**  
1. https://unix.stackexchange.com/a/99435

