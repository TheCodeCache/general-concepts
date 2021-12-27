# General Terms and Notes:

a.) The action of caching files when accessing them the first time is called `disk buffering`  
b.) When a file is read, the data are put into the `page cache`  
c.) We can use `iostat`, `vmstat`, and `sar` commands to check disk I/O performance.  
d.) We can also check disk read and write activity by process using the `iotop` command.  
e.) **page cache**: It is that certain amount of system memory that the kernel reserves for caching the file system disk accesses  
This is to make overall performance faster,  
f.) The Linux uses `write-back` approach for caching, and not `write-through`, the former is better in performace but error prone in failover cases.    
g.) **buffer**: a buffer is an area of memory used to temporarily store data while being moved from one place to another  
In addition, the `buffer` contains the `metadata of the files` or data which resides under the `page cache`  
h.) a `cache` is a temporary storage area to store frequently accessed data for rapid access.  


