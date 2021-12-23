# CPU load statistics

We can use **`mpstat -P ALL`** command in linux to know about CPU load/usage for each core separately.  

The below cpu load snapshot is taken,  
when large numbers of small files were being uploaded from local unix ec2 machine to aws s3 storage.  
using the below cmd:
```bash
$ aws s3 cp --recursive --quiet . s3://test_bucket/test_smallfiles/
```

CPU load stats:  

```bash
$ mpstat -P ALL 10
Linux 3.14.35-28.38.amzn1.x86_64 (ip-10-0-0-37)     05/04/2015  
_x86_64_    (4 CPU)

<SNIP>
09:43:18 PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
09:43:19 PM  all    6.33    0.00    1.27    0.00    0.00    0.00    0.51    0.00   91.90
09:43:19 PM    0   14.14    0.00    3.03    0.00    0.00    0.00    0.00    0.00   82.83
09:43:19 PM    1    6.06    0.00    2.02    0.00    0.00    0.00    0.00    0.00   91.92
09:43:19 PM    2    2.04    0.00    0.00    0.00    0.00    0.00    1.02    0.00   96.94
09:43:19 PM    3    2.02    0.00    0.00    0.00    0.00    0.00    1.01    0.00   96.97
```

The system is not seriously stressed given the small file sizes involved.  
Overall, the CPU is 91.90% idle.  
We don’t see any %iowait, %sys, or %user activity,  
so, we can assume that almost all of the CPU time is spent running the AWS CLI commands and handling file metadata.  

**Reference:**  
1. https://aws.amazon.com/blogs/apn/getting-the-most-out-of-the-amazon-s3-cli/  
2. https://www.geeksforgeeks.org/mpstat-command-in-linux-with-examples/  

