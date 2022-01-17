from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    return {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }


def add_stamp(passport, country):
    if "stamps" not in passport:
        passport["stamps"] = []

    if country not in passport["stamps"]:
        passport["stamps"].append(country)

    return passport


def add_biometric_data(passport, biometric_data_type, value, date):
    if not "biometric" in passport:
        passport["biometric"] = {}
    biometric_data = {"date": date, "value": value}
    passport["biometric"][biometric_data_type] = biometric_data
    return passport


if __name__ == "__main__":
    # Part 1: Create passport
    countries = get_countries()
    hank = create_passport("Hank Bobbiton", "1980-12-31", "Brussels", 178.52, "Belgium")
    print(hank)

    # Part 2: Add stamp
    hank = add_stamp(hank, countries[0])
    hank = add_stamp(hank, countries[32])
    print(hank)

    # Part 3: Add biometric data
    omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
    omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
    omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
    print(omari)

    # Omari gets a new left eye because of an accident
    omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")
    print(omari)

    # Add fingerprints too: just another value, but this is also a dict.
    fingerprint_data = {
        "left_pinky": "2378945",
        "left_ring": "2349081",
        "left_middle": "132890",
        "left_index": "9823234",
        "left_thumb": "0924131",
        "right_thumb": "6234923",
        "right_index": "13249734",
        "right_middle": "34023784",
        "right_ring": "12332538",
        "right_pinky": "32458970",
    }
    omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
    print(omari)
