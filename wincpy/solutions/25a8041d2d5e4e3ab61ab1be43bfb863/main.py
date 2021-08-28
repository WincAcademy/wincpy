from helpers import get_countries

__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"


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

    if country not in passport["stamps"] and country != passport["nationality"]:
        passport["stamps"].append(country)

    return passport


def check_passport(
    passport,
    destination_country,
    allowed_destinations_per_country,
    forbidden_origins_per_country,
):
    nationality = passport["nationality"]
    if destination_country in allowed_destinations_per_country[nationality]:
        if destination_country in forbidden_origins_per_country:
            if nationality in forbidden_origins_per_country[destination_country]:
                return False
            if "stamps" in passport:
                for stamp in passport["stamps"]:
                    if stamp in forbidden_origins_per_country[destination_country]:
                        return False
        return add_stamp(passport, destination_country)
    return False


if __name__ == "__main__":
    countries = get_countries()
    hank = create_passport("Hank Bobbiton", "1980-12-31", "Brussels", 178.52, "Belgium")
    print(hank)
    hank = add_stamp(hank, countries[0])
    hank = add_stamp(hank, countries[32])
    print(hank)

    hank = check_passport(
        hank,
        "The Netherlands",
        {"Belgium": ["The Netherlands"]},
        {"The Netherlands": ["North Korea"]},
    )
    print(hank)

    hank = add_stamp(hank, "North Korea")
    print(hank)

    print(
        check_passport(
            hank,
            "The Netherlands",
            {"Belgium": ["The Netherlands"]},
            {"The Netherlands": ["North Korea"]},
        )
    )
