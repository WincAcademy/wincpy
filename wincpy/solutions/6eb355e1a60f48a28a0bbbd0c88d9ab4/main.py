__winc_id__ = "6eb355e1a60f48a28a0bbbd0c88d9ab4"
__human_name__ = "lists"


def alphabetical_order(films):
    return sorted(films)


def won_golden_globe(film_name):
    winners = [
        "jaws",
        "star wars: episode iv - a new hope",
        "e.t. the extra-terrestrial",
        "memoirs of a geisha",
    ]
    return film_name.lower() in winners
