# Subshell:  
When a command is executed in shell/bash inside a set of parenthesis it spawns a new process, which is `Subshell`.  
  For ex:  
```shell
  #!/bin/sh
  echo "output before exit"

  # This `subshell` will not cause the parent process to exit
  (exit 1)

  echo "output after exit"
```  
If we run the above script, we will get the result like below:
```
  output before exit
  output after exit
```
This subshell `(exit 1)` did not result into parent shell to exit, because the `subshell` doesn’t have access to quit the parent shell.  

We need to use `signals` to exit from the parent shell.  

```shell
  #!/bin/sh

  trap "exit 1" 10
  PROC="$$"

  fatal(){
    echo "$@" >&2
    kill -10 $PROC
  }

  echo "output before exit"
  (fatal "no more output, script exiting")
  echo "output after exit"

```
This results in below output:  
```
  output before exit
  no more output, script exiting
```

# Signal:

**What happends when we press ctrl+c on the unix/linux shell:**  

 Processes in `*nix` based operating systems can respond to `signals` to perform an action from outside the process.  
 This is the mechanism that allows you to exit a command line process by pressing `ctrl-c`.  
 When you press `ctrl-c` in your terminal, an `interrupt signal`, for ex: `SIGINT`, is sent to the current process.  
 The process then responds to that `signal` by exiting (if it’s a well behaved process).  

We can run `trap -l` to check all the signals supported by the system,  

Here is the list:  
 in the format: `signal-pre-defined-number) signal-name`
```
   1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
   6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
  11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
  16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
  21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
  26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
  31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
  38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
  43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
  48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
  53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
  58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
  63) SIGRTMAX-1  64) SIGRTMAX
```

**How to respond to a signal using trap:**  

```shell
  #!/bin/sh

  # 2 is the SIGINT signal
  trap 'echo "received SIGINT"' 2
  # This could also be written as:
  # trap 'echo "received SIGINT"' INT

  # Note, SIGINT will be sent to child jobs, so the sleep
  # process will be interrupted when SIGINT is received.
  sleep 30

  echo "echo after sleep finishes"
```
This results in something like below, 'notice, we pressed ctrl+c i.e. ^C'  
```^Creceived SIGINT
echo after sleep finishes
```
**Example:**  
Save the following as `test.sh` and make it executable with `chmod +x test.sh`  
```shell
  #!/bin/sh

  # fatal uses SIGUSR1 to allow clean fatal errors
  trap "exit 1" 10
  PROC=$$
  fatal(){
    echo "$@" >&2
    kill -10 $PROC
  }

  test -n "$1" || fatal "you must provide a path to a file as the first argument"

  test -f $1 || fatal "'${1}' isn't a file"

  (fatal "'${1}' pointed to a file, good job, but we're proving the subshell fatals too")

  echo "This should never output"
```

Reference:
1. https://cravencode.com/post/essentials/exit-shell-script-from-subshell/

