What happens when we type "ls -l *.txt" from a directory on linux machine?  



At high level, the following steps are involved:  

1. The command is entered and if it’s length is not-null, then it is kept in history (memory):  
    The command is entered into the terminal and if it is not null (empty),  
      then memory is allocated for it’s storage.  
      It is also stored as part of the log’s history in case you want to see what command was entered at a certain time.  
      An example of a null command would be when you just click enter on the terminal.  
      If this happens, then steps 2 to 6 will be skipped and the terminal will go straight to step 7.  
2. Parsing:  
    It'll simply parse the given command, and create the abstract syntax tree,  
3. Checking for special characters like pipes:  
    By piping, the output of one process becomes the input of another process, This is done by the piping character '|'.  
      Pipes are unidirectional and data flows from left to write  
4. Checking if built-in commands are asked for:  
    Built in commands are stored in a library  
5. Handling pipes if present:  
    It is mostly handled using the pipe() system call  
6. Executing system commands & libraries by forking a child and execvp:  
    System commands and libraries are executed using system calls, System calls are the only entry points into the kernel system.  
      All programs needing resources must use system calls. Some of the services provided by system calls are:  
        - Process creation and management  
        - Main memory management  
        - File access, Directory and File system management  
        - Handling device I/O (Input/output)  
        - Protection  
        - Networking  
    The fork() system call is used to create a new process called a child process that runs concurrently with the process that made it (parent process).  
    After a new child process is created, both processes will execute the next instruction following the fork() system call.  
    A child process uses the same pc(program counter), same CPU registers, same open files which are used in the parent process.  
        One can use the execvp () call to differentiate the processes run by the parent and child processes.  
  
7. Printing current directory name and asking for next input:  
    displays the current directory name and a prompt for the next command(usually $)  
  
This is how the linux shell interprets a command!  
  
**Reference:**  
    - https://medium.com/@b.mugure/what-exactly-happens-when-you-type-ls-l-c-and-hit-enter-in-a-shell-e5516aea4436

