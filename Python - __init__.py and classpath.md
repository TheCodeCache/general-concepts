# ToDo:

# __ init __.py

The primary purpose of this file is turning a folder into python recognized directory to search for files or scripts.

The `__init__.py` files are required to make Python treat the directories as containing packages;  
this is done to prevent directories with a common name, such as string,  
from unintentionally hiding valid modules that occur later on the module search path.  
In the simplest case, `__init__.py` can just be an empty file,  
but it can also execute initialization code for the package or set the `__all__` variable, described later.


**Reference:**  
1. https://stackoverflow.com/a/35950839/6842300

