# Create CPU load/stress in Linux - 

# using `yes` cmd
Run `yes` cmd like below a few times, and check with `top` command for the cpu usage  
`yes > /dev/null &`  

It can also be used to test how well a system handles high loads,  
as using `yes` results in 100% processor usage, for systems with a single processor (for a multiprocessor system, a process must be run for each processor).  
This, for example, can be useful for investigating whether a system's cooling system will be effective when the processor is running at 100%.  

# using `stress` cmd

we can also use `stress` command for test load on server like below -  

`stress --cpu 2 timeout 60`  

we may need to install `stress` command that we could simply do using `yum -y install stress`  


**Reference:**  
1. https://en.wikipedia.org/wiki/Yes_%28Unix%29

