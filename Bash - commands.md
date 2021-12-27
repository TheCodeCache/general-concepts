# unix commands 

# System Monitoring Commands - 

**System resources:**  

**`lsof`**:  
  We can use the Linux `lsof` command to capture the number of open connections on a given port port for ex: `443`  
  the cmd to be used as follows:  
  `lsof -i tcp:443`  

  usecase - when we upload a big file to `Amazon S3`, it uploads in chunks (using `multi-part` upload option),  
  so, `lsof` cmd will tell us how many connections are used to upload in chunks at a given port #  

  The `lsof` command will print out a list of every file that is in use.  
  Since Linux considers everythihng a file, this list can be very long.  
  However, this command can be useful in diagnosing problems.  
  
  An example of this is if we wish to unmount a filesystem, but we are being told that it is in use.  
  We could use this command and grep for the name of the filesystem to see who is using it.

  Or suppose we want to see all files in use by a particular process. To do this we would use `lsof -p <processid>`, where <processid> is the process-id  

**`top`**:  
  The `top` will display a continually updating report of system resource usage.  
  ![image](https://user-images.githubusercontent.com/26399543/147449340-a3bde560-8340-49b0-bc8f-d9f5706ce439.png)

  We can modify the output of top while is is running. If we hit an `i`, `top` will no longer display idle processes.  
  Hit `i` again to see them again. Hitting `M` will sort by memory usage, `S` will sort by how long they processes have been running, and `P` will sort by CPU usage again.  

  For more in-depth information about processes you can look in the `/proc` filesystem.  
  In the `/proc` filesystem we will find a series of sub-directories with numeric names.  
  These directories are associated with the processes ids of currently running processes.  
  In each directory we will find a series of files containing information about the process.  

  ![image](https://user-images.githubusercontent.com/26399543/147450249-ec35da51-8187-4505-8711-a6444f81d607.png)
  
  NOTE: WE MUST TAKE EXTREME CAUTION TO NOT MODIFY THESE FILES, DOING SO MAY CAUSE SYSTEM PROBLEMS!  

**`iostat`**:  
  ![image](https://user-images.githubusercontent.com/26399543/147449271-da32a47f-729d-48ae-879c-eb2f590c91ff.png)
  
**`ps`**:  
  The ps will provide you a list of processes currently running.  
  A common use would be to list all processes currently running. To do this you would use the `ps -ef` command.  
  
**`vmstat`**:  
  The vmstat command will provide a report showing statistics for system processes, memory, swap, I/O, and the CPU.  
  These statistics are generated using data from the last time the command was run to the present.  
  In the case of the command never being run, the data will be from the last reboot until the present.  
  
  ![image](https://user-images.githubusercontent.com/26399543/147449618-65fe3c34-263b-4708-a4da-0843e6c240ec.png)
  
  ![image](https://user-images.githubusercontent.com/26399543/147449660-3744f4e8-3ca1-4dc7-836f-a3301786ef61.png)  
  
# Filesystem Usage

**`df`**:  
  The `df` is the simplest tool available to view disk usage.  
  Simply type in `df` and we'll be shown disk usage for all your mounted filesystems in 1K blocks  

  ![image](https://user-images.githubusercontent.com/26399543/147450368-a636b721-7d06-4049-a02d-f8f99e2f469b.png)

**`du`**:  
  Now that we know how much space has been used on a filesystem how can we find out where that data is?  
  To view usage by a directory or file we can use `du`. Unless we specify a filename `du` will act recursively.  
  
  ![image](https://user-images.githubusercontent.com/26399543/147450547-ec991181-135b-42bf-8d51-2ee4de429198.png)
  
  
# Monitoring Users 

**`who`**:  
  The easiest way to see `who is on the system` is to do a `who` or `w`.  
  The --> `who` is a simple tool that lists out who is logged --> on the system and what `port` or `terminal` they are logged on at.  
  
  ![image](https://user-images.githubusercontent.com/26399543/147450703-93dd1429-576b-4879-9086-6aee4d7d22f0.png)

**`ps`**:  
  In the previous section, we can see that user `aweeks` is logged onto both pts/1 and pts/2,  
  but what if we want to see what they are doing?  
  We could to a `ps -u aweeks` and get the following output  
  ![image](https://user-images.githubusercontent.com/26399543/147450762-a97063aa-120c-400e-b924-6a30ffec771c.png)

**`w`**:  
  Even easier than using the `who` and `ps -u` commands is to use the `w`.  
  `w` will print out not only who is on the system, but also the commands they are running.  
  
  ![image](https://user-images.githubusercontent.com/26399543/147451120-e8c05f8b-60d0-4114-b529-b23d39cacc1d.png)
  
  
