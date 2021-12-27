# Running Multiple Processes in Parallel - 

To parallelize operations,  
we can use the `-P` option to specify the number of parallel processes used in executing the commands over the input argument list.  

Let’s use it to parallel encode a series of wav files to mp3 format:  

```shell
$find . -type f -name '*.wav' -print0 | xargs -0 -P 3 -n 1 mp3 -V8
```

The encoding process executes using three processes, since -P 3 is specified.

**using `parallel` cmd:**  
It is found in the `moreutils` package.  
```
parallel -j 2 -- 'lsyncd lsyncd.lua' 'webpack --progress --color -w' 
```
these prallel process runs in the foreground.  


**using `&` and `wait`:**  

Code examples:  

```shell
#!/bin/bash
# Our custom function
cust_func(){
  echo "Do something $1 times..."
  sleep 1
}
# For loop 5 times
for i in {1..5}
do
	cust_func $i & # Put a function in the background
done
 
## Put all cust_func in the background and bash 
## would wait until those are completed 
## before displaying all done message
wait 
echo "All done"
```
Example-2 (download files in parallel)  
```shell
#!/bin/bash
# Our custom function
cust_func(){
  wget -q "$1"
}
 
while IFS= read -r url
do
        cust_func "$url" &
done < list.txt
 
wait
echo "All files are downloaded."
```

# GNU parallel examples - 
>GNU parallel is a shell tool for executing jobs in parallel using one or more computers.  
A job can be a single command or a small script that has to be run for each of the lines in the input.  
The typical input is a list of files, a list of hosts, a list of users, a list of URLs, or a list of tables.  

to install on RHEL/CentOS/Fedora based Linux distributions:  
```shell
sudo yum install parallel
```
sample example -  
```shell
cat list.txt | parallel -j 4 wget -q {}
# or
parallel -j 4 wget -q {} < list.txt
```
**Reference:**  
1. https://www.baeldung.com/linux/xargs#4-enable-multiple-process-usage
2. https://askubuntu.com/a/710753
3. https://www.slashroot.in/how-run-multiple-commands-parallel-linux

