"""

File: 
    inspyred_hints/common/interactive/__init__.py

Author: 
    Inspyre Softworks
    
"""
import sys

__all__ = [
    'is_interactive',
    'simulate_enter_keypress'
]


def is_interactive():
    """
    Returns True if the current environment is interactive, False otherwise.
    """
    return sys.__stdin__.isatty() and sys.__stdout__.isatty() and sys.__stderr__.isatty()


def simulate_enter_keypress():
    """
    Simulates an enter keypress.
    """
    sys.__stdout__.write('\n')
    sys.__stdout__.flush()
