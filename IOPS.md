# What are IOPS — 

Input/Output Operations Per Seconds:  
it's pretty useful to measure at ranfom workloads  
![image](https://user-images.githubusercontent.com/26399543/147840242-583bf48f-486b-4e6e-9340-9773ee08021c.png)

In the above image,  
we 've random read capacity of <= 500k IOPS
we 've random write capacity of <= 480k IOPS

![image](https://user-images.githubusercontent.com/26399543/147840266-513255d0-0196-41c0-8681-c66507dfd17c.png)

In the above image:  
Block-Size & Concurrency depend on Software,  
Throughput & Latency are deteremined by Hardware,  

![image](https://user-images.githubusercontent.com/26399543/147840446-da12d611-8847-4fa0-9718-19daad7e200a.png)

**Usecase/Trade-Offs** -  

- High Random IOPS are good for RDBMS like Oracle/MySQL etc,  
because reading a row/record from table/views is random  
- High Sequential IOPS are good for DataWarehouses,  
as they generally work on a batch of rows  

**Reference:**  
1. https://recoverymonkey.org/2012/07/26/an-explanation-of-iops-and-latency/
2. https://louwrentius.com/understanding-storage-performance-iops-and-latency.html

