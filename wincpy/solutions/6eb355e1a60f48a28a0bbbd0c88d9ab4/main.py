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


def remove_toto_albums(mess):
    # Reader has not yet had instruction about for-loops.
    # If you have: how could you improve this code by making use of them?
    if "Fahrenheit" in mess:
        mess.remove("Fahrenheit")
    if "The Seventh One" in mess:
        mess.remove("The Seventh One")
    if "Toto XX" in mess:
        mess.remove("Toto XX")
    if "Falling in Between" in mess:
        mess.remove("Falling in Between")
    if "35th Anniversary - Live in Poland" in mess:
        mess.remove("35th Anniversary - Live in Poland")
    if "Toto XIV" in mess:
        mess.remove("Toto XIV")
    if "Old Is New" in mess:
        mess.remove("Old Is New")
    if "40 Tours Around The Sun - Live in Holland" in mess:
        mess.remove("40 Tours Around The Sun - Live in Holland")
    return mess
