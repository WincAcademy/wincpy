""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"


def run(student_module):
    result = []

    # Shortaciousness
    sm = student_module

    passport = sm.create_passport(
        "Hank Bobbiton", "1980-12-31", "Brussels", 178.52, "Belgium"
    )
    result.append(
        (
            "create_passport is correct",
            passport
            == {
                "name": "Hank Bobbiton",
                "date_of_birth": "1980-12-31",
                "place_of_birth": "Brussels",
                "height": 178.52,
                "nationality": "Belgium",
            },
        )
    )

    passport = sm.add_stamp(passport, "Belgium")
    passport = sm.add_stamp(passport, "Afghanistan")
    passport = sm.add_stamp(passport, "Bulgaria")
    result.append(
        (
            "add_stamp is correct",
            "stamps" in passport
            and "Afghanistan" in passport["stamps"]
            and "Bulgaria" in passport["stamps"]
            and "Belgium" not in passport["stamps"],
        )
    )

    allowed_destinations_per_country = {"Belgium": ["The Netherlands", "Bulgaria"]}
    forbidden_origins_per_country = {"The Netherlands": ["Afghanistan"]}
    result.append(
        (
            "check_passport is correct",
            not sm.check_passport(
                passport,
                "The Netherlands",
                allowed_destinations_per_country,
                forbidden_origins_per_country,
            )
            and sm.check_passport(
                passport,
                "Bulgaria",
                allowed_destinations_per_country,
                forbidden_origins_per_country,
            )
            == sm.add_stamp(passport, "Bulgaria"),
        )
    )

    return result
