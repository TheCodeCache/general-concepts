
# Calculating CPU Usage -

**Method-1:**  
`The vmstat command displays CPU activity in near-real time:`  
```shell
[root@localhost ~]# vmstat 3 4
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 4  0      0 1347080   6120 941464    0    0    68    11   72  137  1  2 97  0  0
 1  0      0 1347080   6120 941464    0    0     0     0   84  157  1  2 97  0  0
 1  0      0 1347080   6120 941464    0    0     0     0   59  107  1  1 98  0  0
 1  0      0 1347080   6120 941464    0    0     0     1   59  104  1  1 98  0  0
```
The columns under CPU provide an overview of where the processor time is spent:
- us – time spent running non-kernel code
- sy – time spent running kernel code
- id – time spent idle
- wa – time spent waiting for I/O
- st – time is stolen from a virtual machine
The `id` column is what we’re interested in.  
With the delay of a second, we **calculate the CPU usage** using vmstat:  

```shell
[root@localhost ~]# echo "CPU Usage: "$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]"%"
CPU Usage: 2%
```
Note: The vmstat command without any arguments provided will give CPU times since boot  

**Method-2:**  
CPU activity can also be extracted from the `/proc/stat` file. The file contains various metrics about the system since boot:  

```
[root@localhost ~]# cat /proc/stat 
cpu  3020 28 1863 22404 35 432 47 0 0 0
cpu0 3020 28 1863 22404 35 432 47 0 0 0
intr 96468 28 100 0 0 0 0 0 0 1 0 0 0 1263 0 0 0 3696 0 153 928 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 207 0 41 14600 0 0 0 0 0 0 0 0 0 0 0 0 0 0 343 97 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 340950
btime 1628404433
processes 3276
procs_running 2
procs_blocked 0
softirq 112867 1 16857 56 269 510 0 261 0 0 94913
```
The first line, `cpu` is an aggregate of the metrics of all cores of the system.  
On a system with 4 cores, there would be 4 cpu lines — cpu0, cpu1, cpu2, and cpu3.  
The columns in the `cpu` row represent times spent processing different tasks:  

- user – time spent in user mode
- nice – time spent processing nice processes in user mode
- system – time spent executing kernel code
- idle – time spent idle
- iowait – time spent waiting for I/O
- irq – time spent servicing interrupts
- softirq – time spent servicing software interrupts
- steal – time stolen from a virtual machine
- guest – time spent running a virtual CPU for a guest operating system
- guest_nice – time spent running a virtual CPU for a “niced” guest operating system

We’re going to use these metrics to calculate the average idle percentage  

Average idle time (%) = (idle * 100) / (user + nice + system + idle + iowait + irq + softirq + steal + guest + guest_nice)  

```shell
cat /proc/stat |grep cpu |tail -1|awk '{print ($5*100)/($2+$3+$4+$5+$6+$7+$8+$9+$10)}'|awk '{print "CPU Usage: " 100-$1}'
CPU Usage: 2.4219
```
Since, we're working on a single-core system, the 'cpu' line will be the same as 'cpu1'.  
Hence, the use of `tail -1` is to retrieve only one of the lines.  
Yet, we'd use the 'cpu' line on a multiprocessor system since it's an aggregate of metrics on all cores.  

**Method-3:**  
Generally, the `top` command is usually utilized to display active processes on a system,  
and how much resources the processes are consuming.  
Nevertheless, we can use this command to measure the state of the CPU:  

```shell
[root@localhost ~]# top

top - 07:08:31 up  2:41,  1 user,  load average: 0.00, 0.00, 0.00
Tasks: 322 total,   2 running, 320 sleeping,   0 stopped,   0 zombie
%Cpu(s): 10.0 us, 15.0 sy,  0.0 ni, 97.8 id,  0.0 wa,  5.0 hi,  0.0 si,  0.0 st
MiB Mem :   3709.4 total,   1483.1 free,   1402.0 used,    824.4 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   2053.4 avail Mem 
```
Note - it's important to note that the `top` command displays the CPU percentage of a single core.  
In a multiprocessor system, it's possible to have the CPU percentage exceed 100%.  
For example, if 4 cores are at 75%, the top command will show CPU as being 300%.  

We need to obtain the value of the time spent being idle so that we can subtract it from 100 to get the usage  

```shell
[root@localhost ~]# top -bn2 | grep '%Cpu' | tail -1 | grep -P '(....|...) id,'|awk '{print "CPU Usage: " 100-$8 "%"}'
CPU Usage: 2.2%
```
The `-n` option is the number of iterations the `top` command should use before ending.  
We avoid using the first loop because the metrics we retrieve will be values since boot.  
Hence, we've taken the second iteration.  

Also, in a multiprocessor system, we'd have to divide the given 'id' value by the number of cores and subtract the value from 100  
For example, if we were operating on a quad-core system and the 'id' value was 304%, we'd calculate our CPU usage as:  
**CPU Usage % = 100 – (304/4)**

```shell
[root@localhost ~]# top -bn2 | grep '%Cpu' | tail -1 | grep -P '(....|...) id,'|awk '{print "CPU Usage: " 100-($8/4) "%"}'
```

**Reference:**  
1. https://www.baeldung.com/linux/get-cpu-usage

