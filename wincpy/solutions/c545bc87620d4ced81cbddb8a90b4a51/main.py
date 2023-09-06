from helpers import get_countries

__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


def shortest_names(countries):
    shortest = min(countries, key=len)
    shortest_names = []
    for country in countries:
        if len(country) == len(shortest):
            shortest_names.append(country)
    return(shortest_names)


def most_vowels(countries):
    vowels = "aeiou"

    # List of tuples of (country_name, vowel_count)
    # Can also be lists if unfamiliar with tuples
    leaderboard = [("", 0)]

    for country_name in countries:
        # Count vowels
        vowel_count = 0
        for char in country_name:
            if char.lower() in vowels:
                vowel_count += 1

        # Insert into leaderboard if deserving.
        for position in range(len(leaderboard)):
            if vowel_count >= leaderboard[position][1]:
                leaderboard.insert(position, (country_name, vowel_count))
                break
            if position > 2:
                break

    return [x[0] for x in leaderboard[:3]]


def alphabet_set(countries):
    # Assembles alphabet
    countries = [country.lower() for country in countries]

    letters_needed = list("abcdefghijklmnopqrstuvwxyz")
    countries_used = []
    for country in countries:
        for char in country:
            if char in letters_needed:
                letters_needed.remove(char)
                if country not in countries_used:
                    countries_used.append(country)
        if len(letters_needed) == 0:
            return countries_used


""" This block is only run if this file is called directly from the command line. """
if __name__ == "__main__":
    countries = get_countries()
    # You can run your own tests here.
    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))
    print(len(alphabet_set(countries)))
