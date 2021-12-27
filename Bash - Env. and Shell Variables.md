# Overview - 

Each Linux process has its own set of environment variables, which it inherits from its parent.  
For example, when we execute a command in our shell, the command inherits the environment variables of the shell.  

and we can manage them using `env`, `printenv`, and `export`.  

# Global Environment Variables - 
When we start a shell, we create our shell with a set of predefined environment variables  
We can declare them globally or on a per-user basis.  

With `Bash`, we declare global variables in `/etc/profile`.  
but, it's recommended to declare them in their own script files and putting those in `/etc/profile.d`.  
Bash will automatically pick these up.  

Each user can create a set of 'global' environment variables for their own by creating `~/.profile` in their `home` directory.  

One of the most common environment variables we use on a daily basis is the `PATH` variable.  
and this is how we append other locations to `PATH` variable  
```shell
PATH=$PATH:/path/to/executable/
```

# `env` and `printenv` - 
We can use env to run a program in a modified environment, by supplying additional environment variables:  
```shell
env CUSTOM_VAR=42 /path/to/script.sh
```
In this example, `env` will execute /path/to/script.sh in an environment,  
that is a copy of our shell environment with CUSTOM_VAR as an added environment variable with value 42.  
here's another way to declare multiple variables:  
```shell
env VAR_ONE=1 VAR_TWO=2 /path/to/script.sh
```
We can also unset or remove variables by preceding them with `-u`:  
Th below code will run our script in a copy of the current environment, but without the PATH variable.  
```shell
env -u PATH /path/to/script.sh
```

This will run the script in an empty environment  
```shell
env -i /path/to/scripts.sh
```

to use `printenv` :  
```shell
printenv HOSTNAME PATH HOME
```
the above will print the values of the variables: hostname, path and home  


# Shell Variables - 
We should not confuse `environment variables` with `shell variables`.  
`Shell variables` are variables that apply to our current shell only and are not inherited by any programs or scripts that we execute.  

We can get an overview of all variables that apply to our current shell by calling `set` -  

```shell
[vagrant@localhost ~]$ set
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:expand_aliases:extquote:force_fignore:histappend:hostcomplete:interactive_comments:login_shell:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
BASH_CMDS=()
BASH_LINENO=()
HOSTNAME=localhost.localdomain
TERM=xterm-256color
SHELL=/bin/bash
HISTSIZE=1000SSH_TTY=/dev/pts/0
USER=vagrant
MAIL=/var/spool/mail/vagrant
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/vagrant/.local/bin:/home/vagrant/bin
PWD=/home/vagrant
LANG=en_US.UTF-8 HOME=/home/vagrant
LOGNAME=vagrant
```

Shell variables aren't inherited by subprocesses, but we can `export` them to make them visible  

**Reference:**  
1. https://www.baeldung.com/linux/environment-variables

