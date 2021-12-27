# `cron` service - 

Everyone who has ever worked on Linux, must have heard of `cron` expression, which is used to schedule tasks execution at certain intervals.  

`cron` is a generic software service for scheduling tasks.  
It comprises two key components: 
`cron daemon` (`crond`) and `cron configuration`.  
`crond` reads the `cron configuration` to determine when to run which task.  
It iterates all the files under `/var/spool/cron`, `/etc/crontab`, and `/etc/cron.d` to execute the commands.  

`crontab` is the `command-line utility` to manage all cron jobs.  
The `cron packages` are available by default in all recent Linux variant systems. If not, we can install it using a package manager.  

the expression syntax is as follows -  
`# [minute] [hours] [day of month] [month] [day of the week] command-to-execute`  

# `at` service - 
This allows us to execute commands at a specific time, but only once.  
**Examples** -  
```shell
$ date
Wed Aug 25 06:49:57 IST 2021
$ date > current-time.txt | at now
warning: commands will be executed using /bin/sh
job 9 at Wed Aug 25 06:50:21 2021
$ cat current-time.txt
Wed Aug 25 06:50:22 IST 2021
```
in the above `date > current-time.txt` - this will create a new file named 'current-time.txt' and writes the current date into it `at now`.  

to schedule a shell script, we can use like below:  
```shell
$ at 09:00 -f /home/baeldung/one-time-env-setup.sh
```

# `batch` service - 

the `batch` command is an extended feature of the `at` command.  
It `executes a command based on CPU load` and not on time parameters  

# security aspects - 

We can restrict the users accessing the at and batch services using `/etc/at.deny` and `/etc/at.allow` files.  

Now, let's block the user jack from accessing at and `batch` services by simply adding the username into the `/etc/at.deny` file:  

```shell
root@sandbox1:~$ cat /etc/at.deny | grep jack
jack

jack@sandbox1:~$ at
You do not have permission to use at.

jack@sandbox1:~$ batch
You do not have permission to use at.
```


**Reference:**  
1. https://www.baeldung.com/linux/schedule-script-execution

