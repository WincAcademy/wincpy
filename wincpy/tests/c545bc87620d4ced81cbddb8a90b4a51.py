""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import (compare_states, exec_assignment_code,
                            get_main_abspath)

__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'


def run(student_module):
    result = []

    # Shortify
    sm = student_module

    requirement = 'shortest_names() is correct'
    result.append((requirement,
                   sm.shortest_names(sm.get_countries())
                   == ['Chad', 'Cuba', 'Guam', 'Iran', 'Iraq', 'Laos', 'Mali',
                       'Niue', 'Oman', 'Peru', 'Togo']))

    requirement = 'most_vowels() is correct'
    result.append((requirement,
                   sm.most_vowels(sm.get_countries())
                   == ['South Georgia and the South Sandwich Islands',
                       'Micronesia, Federated States of',
                       'The Democratic Republic of Congo']))

    return result
