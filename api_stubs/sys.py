"""
|see_cpython_module| :mod:`python:sys`.
"""

def exit(retval=0):
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    pass

def atexit(func):
    """
    Register *func* to be called upon termination.  *func* must be a callable
    that takes no arguments, or ``None`` to disable the call.  The ``atexit``
    function will return the previous value set by this function, which is
    initially ``None``.
    .. admonition:: Difference to CPython
       :class: attention
       This function is a MicroPython extension intended to provide similar
       functionality to the :mod:`atexit` module in CPython.
    """
    pass

def print_exception(exc, file=sys.stdout):
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).
    .. admonition:: Difference to CPython
       :class: attention
       This is simplified version of a function which appears in the
       ``traceback`` module in CPython. Unlike ``traceback.print_exception()``,
       this function takes just exception value instead of exception type,
       exception value, and traceback object; *file* argument should be
       positional; further arguments are not supported. CPython-compatible
       ``traceback`` module can be found in `micropython-lib`.
    """
    pass

