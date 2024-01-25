"""
Evaluating function output using exceptions

Rouphly following https://github.com/matplotlib/matplotlib/pull/25887#issuecomment-1889843257 as an example
"""

import sys

class A:
    pass

def is_a(var) -> bool:
    try: 
        return  isinstance(var, A)
    except Exception:
        return False
    
def is_some_fancy_object(var) -> bool:
    try:
        return isinstance(var, sys.modules['some_fancy_module'].SomeFancyObject)
    except Exception:
        return False