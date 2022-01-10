# Thread pool with `xargs` — 

There is also a nearly unknown functionality of `xargs` utility.  
It... is capable to act as a `thread pool`! (Well, this would be a process pool, actually.)  
Given a lot of arguments, it is capable to maintain the fixed number of processes that will be invoked for these arguments sequentially,  
picking next one from standard input of xargs when one of the processes finishes execution..  

**Reference:**  
1. http://coldattic.info/post/7/

