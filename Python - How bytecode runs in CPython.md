This is quite well explained here:  
  
Question:  
  https://stackoverflow.com/questions/19916729/how-exactly-is-python-bytecode-run-in-cpython  
  I am trying to understand how Python works (because I use it all the time!).   
  To my understanding, when you run something like python script.py,   
  the script is converted to bytecode and then   
  the interpreter/VM/CPython–really just a C Program–reads in the python bytecode and executes the program accordingly.  
  
  How is this bytecode read in?   
  Is it similar to how a text file is read in C?   
  I am unsure how the Python code is converted to machine code.   
  Is it the case that the Python interpreter (the python command in the CLI) is really just a precompiled C program  
  that is already converted to machine code and then the python bytecode files are just put through that program?   
  In other words, is my Python program never actually converted into machine code?   
  Is the python interpreter already in machine code, so my script never has to be?  
  
Answer:  
  https://stackoverflow.com/a/19916892  
  
CPython (Python interpreter) Code:  
  https://hg.python.org/cpython/file/3.3/Python/ceval.c#l1805  
  
Answer Summary:  
  There is basically (very basically) a giant switch statement inside the CPython interpreter that says   
    "if the current opcode is so and so, do this and that"  
  
Other implementations, like Pypy, have JIT compilation, i.e. they translate Python to machine codes on the fly.  
  
  
  
  
Other Details:  
  https://stackoverflow.com/a/2324217  
  Python is a language.  
  CPython is the default byte-code interpreter of Python, which is written in C.  
  There is also other implementation of Python such as IronPython (for .NET), Jython (for Java), etc.  
    
  This means CPython takes care of converting Python code to Byte Code and also interpret byte code to machine code ? -> YES  
  In nut shell CPython is Compiler (for conversion from Python to Byte Code) and also Python Virtual Machine (for Byte code to Machine code) ? -> YES  
  
