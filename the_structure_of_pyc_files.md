When we compile a python code, it generates `.pyc` file, which is a binary file containing byte codes. \
  It's just like a regular file when it comes to CPython interpreter. \
  The interpreter reads `.pyc` file and for every 'opcode' in the byte-code, it executes a set of machine codes, which are already compiled into interpreter.\
  More details on this topic is captured here: https://github.com/TheCodeCache/general-concepts/blob/master/How-Python-bytecode-runs-in-CPython

At the simple level, a .pyc file is a binary file containing only three things:  
- A four-byte magic number  
- A four-byte modification timestamp  
- A marshalled code object

The action of every agent <br />
  into the world <br />
starts <br />
  from their physical selves. <br />

The magic number is nothing but a two-byte data, that changes with each change to the marshalling code,  
  and then two bytes of 0d0a. The 0d0a bytes are a carriage return and line feed.  

The four-byte modification timestamp is the Unix modification timestamp of the source file that generated the .pyc,  
  so that it can be recompiled if the source changes.  
  
The entire rest of the file is just the output of marshal.dump of the code object that results from compiling the source file  
  
Marshal is like pickle,  
in that it serializes Python objects. It has different goals than pickle, though.  
Where pickle is meant to produce version-independent serialization suitable for persistence,  
  marshal is meant for short-lived serialized objects, so its representation can change with each Python version.  
Also, pickle is designed to work properly for user-defined types,  
  while marshal handles the complexities of Python internal types  
  
When we compile a python program, it returns somthing called 'code object', in general terms, we can also call it as compiled-code or byte-code.  
    
Code objects represent byte-compiled executable Python code, or bytecode.  
  The difference between a code object and a function object is that  
    the function object contains an explicit reference to the function’s globals (the module in which it was defined),  
    while a code object contains no context; also the default argument values are stored in the function object,  
      not in the code object (because they represent values calculated at run-time).  
    Unlike function objects, code objects are immutable and contain no references (directly or indirectly) to mutable objects.  
marshal.dump(codeobject, binaryfile) - where codeobject is the data to bw written on binaryfile,  
  which will later be loaded using marshal.load(..) and be executed using exec(..)  
  
Code Example (working):  
  
```python
'''
marshal code
'''
import marshal
script = """
a = 10
b = 20
print ('addition = ',a+b)
"""
code = compile(script, "script", "exec") # compiles the code
f = open("a.pyc","wb")
marshal.dump(code, f) # marshal
f.close()
  
  
'''
un-marshal code
'''
import marshal
f = open("a.pyc","rb")
data = marshal.load(f)
exec (data)
  
#output: 30
```
compile(...) explanation:  
  The first argument to compile() is the string of Python code to be compiled, which should be obvious.   
  The second defines the "filename" of the piece of code (here, as is conventional, we use <string> to indicate code attained from the interactive shell).  
  The third is the type of compilation,  
    which most often will be 'exec',  
    other mode could be 'eval', which is used for strings containing only a single expression,  
    3rd mode: 'single', in which the generated code object is expected to contain a single statement,  
      whose return value is printed if it is not None (like in the interactive shell).  
  
References:  
- https://late.am/post/2012/03/26/exploring-python-code-objects  
- https://nedbatchelder.com/blog/200804/the_structure_of_pyc_files.html  
- https://www.tutorialspoint.com/internal-python-object-serialization-marshal  
- https://docs.python.org/3/library/marshal.html  
  
  
