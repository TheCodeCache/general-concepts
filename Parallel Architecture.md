# Parallel Architecture

We usually tend to think parallelism means multiple cores, this is not entirely true.  
Modern computers are parallel on many different levels,  

individual cpu cores have been faster every year, until recently,  
i.e. the CPU performance improvements have now slowed down.  
all this have been already predicted by [Moore's Law](https://en.wikipedia.org/wiki/Moore%27s_law)    

1. Bit-Level Parallelism
2. Instruction-Level Parallelism
3. Data Parallelism
   One of the applications that’s most amenable to data parallelism is image processing.  
   To increase the brightness of an image, for example, we increase the brightness of each pixel.  
   For this reason, modern GPUs (graphics processing units) have evolved into extremely powerful data-parallel processors.  
4. Task-Level Parallelism

7 concurrency model:

1. Threads and locks
2. Functional programming
3. The Clojure Way
4. Actors
5. Communicating Sequential Processes
6. Data parallelism
7. The Lambda Architecture
   The Lambda Architecture combines the strengths of MapReduce and stream processing to create an architecture that can tackle a wide variety of Big Data problems  

**Reference:**  
1. Seven Concurrency Models in Seven Weeks - Text Book

