""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'


def run(student_module):
    result = []

    # Shortr
    sm = student_module

    # Do stuff
    requirement = 'alphabetical_order()'
    result.append((requirement, sm.alphabetical_order(['b', 'a', 'c']) == ['a', 'b', 'c']))

    requirement = 'won_golden_globe()'
    result.append((requirement,
                   sm.won_golden_globe('Jeff') is False
                   and sm.won_golden_globe('jaws') is True
                   and sm.won_golden_globe('JAWS') is True
                   and sm.won_golden_globe('memoirs of a geisha') is True
                   and sm.won_golden_globe('test') is False))

    requirement = 'remove_toto_albums()'
    result.append((requirement,
                   sm.remove_toto_albums(['Old is New']) == []
                   and sm.remove_toto_albums([]) == []
                   and sm.remove_toto_albums(['test', 'Old is New']) == ['test']
                   and sm.remove_toto_albums(['test', 'Fahrenheit', 'Old is New']) == ['test']))

    return result
