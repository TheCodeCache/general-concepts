The format of a 'shebang' interpreter directive is as follows  
    #!interpreter [optional-arg]  
  
Shell-Script usually begins with one of the following typical line:  
  
- #!/bin/bash - Execute the file using the `Bash shell`  
- #!/bin/ksh - Execute the file using the `Korn shell`  
- #!/bin/sh - Execute the file using the `Bourne shell`, or a compatible shell, assumed to be in the /bin directory  
- #!/usr/bin/env bash - Execute the file using the `Bash shell`  
- #!/usr/bin/env sh - Execute the file using the `Bourne shell`, or a compatible shell, assumed to be in the /bin directory  
- #!/usr/bin/env python - Execute with a `Python interpreter`, using the env program search path to find it  
- #!/usr/bin/pwsh - Execute the file using `PowerShell`  
- #!/bin/false - `Do nothing, but return a non-zero exit status, indicating failure`.   
    Used to prevent stand-alone execution of a script file intended for execution in a specific context,   
      such as by the `.` command from sh/bash, `source` from csh/tcsh, or as a .profile, .cshrc, or .login file  
  
This first line (#!/bin/bash or #!/bin/sh) has a name.   
It is known as 'she-bang'(shabang) or also sometimes called as 'hashbang' or 'Interpreter Directive'  
  
Among, all the above formats, the best practice is as follows:  
    #!/usr/bin/env bash   
    #!/usr/bin/env sh  
    #!/usr/bin/env python  
  
portability issues:  
    there are unix systems, where the default 'env' is not present in standard location like /usr/bin/env rather it's found under /bin/env,   
    in such cases, the script files won't run as expected bcoz it'd be unable to find the interpreter from the shebang declaration,  
  
**References:**  
    https://en.wikipedia.org/wiki/Shebang_%28Unix%29  
    https://askubuntu.com/a/88314  
    https://unix.stackexchange.com/a/87600  
    https://stackoverflow.com/a/13872064  
      
