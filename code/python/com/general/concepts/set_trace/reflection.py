'''
Created on Nov 5, 2021

We can update the local variables of a function on the fly using set_trace(..)

it feels like java reflection, but it's much more than that, 
as it allows to play with even byte code as well, 
it's awesome as well as scary at the same time

@author: manoranjan
'''

import sys


def square_arguments(frame, event, arg):
    '''
    tamper the local variable of the given function, 
    just squaring it before the actual execution of the function begins
    '''
    print(f'event:{event}')
    
    if event != "call":
        return

    code = frame.f_code
    if code.co_name != "add":
        return

    # read all the local variables and play with it
    for var in frame.f_locals:
        frame.f_locals[var] = frame.f_locals[var] ** 2


def add(a, b):
    return a + b


if __name__ == '__main__':
    # Demo
    
    print(f"add(1, 2): {add(1, 2)}")
    sys.settrace(square_arguments)
    print(f"add(1, 2): {add(1, 2)}")
    sys.settrace(None)
