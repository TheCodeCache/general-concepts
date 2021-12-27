# Create CPU spikes in Linux - 

We can make use of below approaches to create CPU spikes:  
1. using `yes` cmd
2. using `stress` cmd
3. using `dd` cmd

# using `yes` cmd
Run `yes` cmd like below a few times, and check with `top` command for the cpu usage  
`yes > /dev/null &`  

It can also be used to test how well a system handles high loads,  
as using `yes` results in 100% processor usage, for systems with a single processor (for a multiprocessor system, a process must be run for each processor).  
This, for example, can be useful for investigating whether a system's cooling system will be effective when the processor is running at 100%.  

In the above command, if we check our CPU usage, we can see that it only overloads one of our CPUs  
to overload more cores, just pipe together to overload more cores as follows:  

```shell
yes > /dev/null | yes > /dev/null
```
the above will overload 2 cores, to overload `n` cores, we need to pipe the above command `n` times  

# using `stress` cmd

we can also use `stress` command for test load on server like below -  

`stress --cpu 2 timeout 60`  

we may need to install `stress` command that we could simply do using `yum -y install stress`  

# using `dd` cmd

The `dd` utility is available on most Unix-like systems.  
We can copy the contents of `/dev/zero` to `/dev/null` using the `dd` command:  
```shell
$ dd if=/dev/zero of=/dev/null
```
- The if an argument is for specifying the input file  
  in our case, it's /dev/zero, which is a special file that contains an indefinite number of `null` characters  
- The of argument is for specifying the output file  
  in this case, we'll save the contents to `/dev/null`, which is a `void` that discards the contents written to it  

Once we execute the command, we can see that it overloads one of our CPUs.  
However, we can write a script that we can execute more than once at the same time to overload the other cores as well:  

```shell
#!/bin/bash

fulload() {
  dd if=/dev/zero of=/dev/null |
  dd if=/dev/zero of=/dev/null |
  dd if=/dev/zero of=/dev/null |
  dd if=/dev/zero of=/dev/null &
};

fulload; read; killall dd
```

we can make the script executable as follows:  
```shell
$ chmod +x ./dd.sh
$ ./dd.sh
```
Once we execute the script, we can observe that it will overload four cores in our system.  
Once we're done, we can press <Enter> or <CTRL-C> to kill the process.  

**Reference:**  
1. https://en.wikipedia.org/wiki/Yes_%28Unix%29

