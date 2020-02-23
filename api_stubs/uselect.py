"""
|see_cpython_module| :mod:`python:select`.
This module provides functions to efficiently wait for events on multiple
`streams <stream>` (select streams which are ready for operations).
"""

def poll():
    """
    Create an instance of the Poll class.
    """
    pass

def select(rlist, wlist, xlist[, timeout]):
    """
    Wait for activity on a set of objects.
    This function is provided by some MicroPython ports for compatibility
    and is not efficient. Usage of :class:`Poll` is recommended instead.
    """
    pass


class ``Poll``:
    """
    Methods
    ~~~~~~~
    """

