# Concurrency Model

1. Processes
2. Threads (system or green)
   `Green threads` are "user-level threads".  
   They are scheduled by an "ordinary" user-level process, not by the kernel.  
   So, they can be used to simulate multi-threading on platforms that don't provide that capability.  
3. Futures
4. Coroutines
5. Communicating sequential processes i.e. CSP
6. Petri Nets.
7. Reactive or Event-driven systems
8. Parallel worker
9. Functional Parallelism
etc.


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
1. http://tutorials.jenkov.com/java-concurrency/concurrency-models.html
2. https://www.youtube.com/watch?v=lPTqcecwkJg
3. Seven Concurrency Models in Seven Weeks - Text Book
