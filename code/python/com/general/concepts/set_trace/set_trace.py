'''
Created on Nov 5, 2021

sys.settrace: 
    sets a trace function that is triggered by the VM every time 
    it enters or exits a function, 
    processes a line of code, runs into an exception and 
    even when it runs a single opcode. 
    Each of these callbacks also give full access to the current stack frame and code.

sys.setprofile:
    sets a trace function that's triggered every time 
    the VM enters or exits both Python and C functions.
    
There are equivalents available in the threading module 
    to allow setting tracers for multi-threaded programs as well: 
    threading.settrace and threading.setprofile.

The frame object contains the current state of computation: 
    all locals, globals, current location, etc.; 
    the code object has the actual opcodes and 
    function details independent of the current stack.

CAUTION:
    it's also possible to modify the state of the program using the frame: 
    so it's possible to override locals, globals, 
    or simply skip around by changing the offset into the bytecode
    
    
API:
    settrace events: call, return, line, exception, opcode
    The trace function has the function signature (frame, event, arg).
    sys.settrace(fn) and sys.setprofile(fn) to set fn as the callback
    sys.settrace(None) and sys.setprofile(None) to clear it.
    
    frame fields
        f_back: previous frame
        f_code: code object
        f_locals: as title
        f_globals: as title
        f_builtins: built-in names
        f_lasti: instruction, index into bytecode string
        f_trace: writable, set the trace function for this frame
        f_trace_lines: writable, trigger trace for each line
        f_trace_opcodes: writable, trigger trace for each opcode
        f_lineno: writable, current line number

    code fields (immutable)
        co_name: function name
        co_argcount: positional arguments
        co_posonlargcount: positional-only arguments
        co_kwonlyargcount: keyword-only arguments
        co_nlocals: # of local variables used by the function, including args
        co_varnames: tuple with names of local variables
        co_cellvars: tuple with local vars referred to by nested functions
        co_freevars: tuple with free variables
        co_code: bytecode as a string
        co_consts: tuple with literals used by bytecode
        first item is docstring or None for functions
        co_names: tuple with names used by bytecode
        co_filename: origin filename
        co_firstlineno: first line number of function
        co_lnotab: maps bytecode offsets to line numbers
        co_flags: flags for interpreter
        0x04: uses *arguments
        0x08: uses **keywords
        0x20: generator
        0x2000: from future import division

Reference:
    https://explog.in/notes/settrace.html

@author: manoranjan
'''

import opcode
import sys
import inspect


def show_trace(frame, event, arg):
    '''
        this show_trace(..) is a simple tracing function to give a live example
    '''
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti

    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")
    return show_trace


def fib(n):
    i, f1, f2 = 1, 1, 1
    while i < n:
        f1, f2 = f2, f1 + f2
        i += 1
    return f1


if __name__ == '__main__':
    header = f"| {'event':10} | {'arg':>4} | line | offset | {'opcode':^18} | {'locals':^35} |"
    print(header)
    sys.settrace(show_trace)
    fib(3)
    sys.settrace(None)
    
    print('\n next experiment (independent from the above) \n')
    
    code = fib.__code__
    print(f"{'field':<20} | value")
    for name, value in inspect.getmembers(code):
        if name.startswith("co_"):
            print(f"{name:<20} | {value}")
