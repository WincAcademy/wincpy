from wincpy.checks.utils import StandardChecks

__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"

TEST_DATA = {
    "name": "Hank Bobbiton",
    "date_of_birth": "1980-12-31",
    "place_of_birth": "Brussels",
    "height": 178.52,
    "nationality": "Belgium",
}


def check_create_passport(student_module):
    StandardChecks.n_params(student_module.create_passport, n_params=5)

    passport = student_module.create_passport(**TEST_DATA)
    assert passport == TEST_DATA, "The returned dict is not as we expected it to be."


def check_add_stamp(student_module):
    StandardChecks.n_params(student_module.create_passport, n_params=5)
    StandardChecks.n_params(student_module.add_stamp, n_params=2)

    passport = student_module.create_passport(**TEST_DATA)
    nationality = TEST_DATA["nationality"]
    assert nationality not in passport.get(
        "stamps", {}
    ), f"Did not expect to find {nationality} in stamps"

    for country in ["Afghanistan", "Bulgaria"]:
        assert country not in passport.get(
            "stamps", {}
        ), f"Did not expect to find {country} in the passport yet"
        passport = student_module.add_stamp(passport, country)
        assert (
            country in passport["stamps"]
        ), f"Expected to find {country} in the passport"


def check_check_passport(student_module):
    StandardChecks.n_params(student_module.create_passport, n_params=5)
    StandardChecks.n_params(student_module.add_stamp, n_params=2)
    StandardChecks.n_params(student_module.check_passport, n_params=4)

    passport = student_module.create_passport(**TEST_DATA)
    for country in ["Afghanistan", "Bulgaria"]:
        passport = student_module.add_stamp(passport, country)
    allowed_destinations_per_country = {
        "Belgium": ["The Netherlands", "Bulgaria", "Denmark"],
    }
    forbidden_origins_per_country = {"The Netherlands": ["Afghanistan"]}

    assert student_module.check_passport(
        passport,
        "Denmark",
        allowed_destinations_per_country,
        forbidden_origins_per_country,
    ).get("stamps", []) == [
        "Afghanistan",
        "Bulgaria",
        "Denmark",
    ], "`check_passport` didn't correctly handle a passport that should receive a stamp"

    assert (
        student_module.check_passport(
            passport,
            "The Netherlands",
            allowed_destinations_per_country,
            forbidden_origins_per_country,
        )
        is False  # Explicit check against `False` is intentional
    ), "`check_passport` approved a passport with a stamp from a forbidden origin"
