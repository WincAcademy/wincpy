""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.checks import utils
from wincpy.checks.utils import StandardChecks

__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"


def check_shortest_names(student_module):
    StandardChecks.n_params(student_module.get_countries, n_params=0)

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
    StandardChecks.n_params(student_module.most_vowels, n_params=1)

    countries = student_module.get_countries()
    assert set(student_module.most_vowels(countries)) == {
        "South Georgia and the South Sandwich Islands",
        "Micronesia, Federated States of",
        "United States Minor Outlying Islands",
    }, "Your top 3 is not correct."


def check_alphabet_set(student_module):
    StandardChecks.n_params(student_module.alphabet_set, n_params=1)

    countries = student_module.get_countries()
    alpha = {chr(i) for i in range(97, 123)}
    provided = set("".join([x.lower() for x in student_module.alphabet_set(countries)]))
    assert provided.issuperset(
        alpha
    ), f"Your set of countries does not provide these letters: {alpha - provided}"
