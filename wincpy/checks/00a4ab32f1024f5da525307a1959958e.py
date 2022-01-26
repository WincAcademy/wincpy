from wincpy.checks.utils import StandardChecks

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"

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


def check_add_biometric_data(student_module):
    StandardChecks.n_params(student_module.create_passport, n_params=5)
    StandardChecks.n_params(student_module.add_biometric_data, n_params=4)

    passport = student_module.create_passport(**TEST_DATA)

    passport = student_module.add_biometric_data(
        passport, "eye_color_left", "blue", "2020-05-05"
    )
    assert "biometric" in passport, "Key `biometric` not found in passport."
    assert (
        "eye_color_left" in passport["biometric"]
    ), "`add_biometric_data` did not add key for given biometric data type"
    assert dict == type(
        passport["biometric"]["eye_color_left"]
    ), "No dictionary found for new biometric data."
    assert (
        "value" in passport["biometric"]["eye_color_left"]
    ), '`add_biometric_data` did not create a "value" key for the given biometric data'

    assert (
        "date" in passport["biometric"]["eye_color_left"]
    ), '`add_biometric_data` did not create a "date" key for the date of recording of the biometric data'

    assert (
        "blue" == passport["biometric"]["eye_color_left"]["value"]
    ), "`add_biometric_data` did not set the correct value for the biometric data"

    assert (
        "2020-05-05" == passport["biometric"]["eye_color_left"]["date"]
    ), "`add_biometric_data` did not set the correct date for the biometric data"

    # Adding another measurement
    passport = student_module.add_biometric_data(
        passport, "eye_color_right", "brown", "2020-06-06"
    )
    assert 2 == len(
        passport["biometric"]
    ), "Adding more biometric data does not result in correct number of biometric data values."
    assert {
        "eye_color_left": {"date": "2020-05-05", "value": "blue"},
        "eye_color_right": {"date": "2020-06-06", "value": "brown"},
    } == passport[
        "biometric"
    ], "Adding more biometric data results in incorrect data on passport."

    # Updating a measurement
    passport = student_module.add_biometric_data(
        passport, "eye_color_left", "green", "2022-01-12"
    )
    assert 2 == len(
        passport["biometric"]
    ), "Updating biometric data does not result in correct number of biometric data values."
    assert {
        "eye_color_left": {"date": "2022-01-12", "value": "green"},
        "eye_color_right": {"date": "2020-06-06", "value": "brown"},
    } == passport[
        "biometric"
    ], "Updating biometric data results in incorrect data on passport."
