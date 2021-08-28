""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"


def run(student_module):
    result = []

    # Shortify
    sm = student_module

    countries = sm.get_countries()
    requirement = "shortest_names() is correct"
    result.append(
        (
            requirement,
            sm.shortest_names(countries)
            == [
                "Chad",
                "Cuba",
                "Guam",
                "Iran",
                "Iraq",
                "Laos",
                "Mali",
                "Niue",
                "Oman",
                "Peru",
                "Togo",
            ],
        )
    )

    requirement = "most_vowels() is correct"
    result.append(
        (
            requirement,
            set(sm.most_vowels(countries))
            == {
                "South Georgia and the South Sandwich Islands",
                "Micronesia, Federated States of",
                "United States Minor Outlying Islands",
            },
        )
    )

    requirement = "alphabet_set() is correct"
    result.append(
        (
            requirement,
            set("".join([x.lower() for x in sm.alphabet_set(countries)])).issuperset(
                set("abcdefghijklmnopqrstuvwxyz")
            ),
        )
    )
    return result
