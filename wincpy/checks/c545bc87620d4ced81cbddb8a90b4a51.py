""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.checks import utils

__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"


def check_shortest_names(student_module):
    countries = student_module.get_countries()
    assert student_module.shortest_names(countries) == [
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
    ]


def check_most_vowels(student_module):
    countries = student_module.get_countries()
    assert set(student_module.most_vowels(countries)) == {
        "South Georgia and the South Sandwich Islands",
        "Micronesia, Federated States of",
        "United States Minor Outlying Islands",
    }, "Your top 3 is not correct."


def check_alphabet_set(student_module):
    countries = student_module.get_countries()
    alpha = {chr(i) for i in range(97, 123)}
    provided = set("".join([x.lower() for x in student_module.alphabet_set(countries)]))
    assert provided.issuperset(
        alpha
    ), f"Your set of countries does not provide these letters: {alpha - provided}"
