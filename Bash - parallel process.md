# Running Multiple Processes in Parallel - 

To parallelize operations,  
we can use the `-P` option to specify the number of parallel processes used in executing the commands over the input argument list.  

Let’s use it to parallel encode a series of wav files to mp3 format:  

```shell
$find . -type f -name '*.wav' -print0 |xargs -0 -P 3 -n 1 mp3 -V8
```

The encoding process executes using three processes, since -P 3 is specified.

**Reference:**  
1. https://www.baeldung.com/linux/xargs#4-enable-multiple-process-usage

