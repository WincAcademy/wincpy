def alphabetical_order(films):
    return sorted(films)


def won_golden_globe(film_name):
    winners = ['jaws',
               'star wars: episode iv - a new hope',
               'e.t. the extra-terrestrial',
               'memoirs of a geisha']
    return film_name.lower() in winners


def remove_toto_albums(mess):
    if 'Fahrenheit' in mess:
        mess.remove('Fahrenheit')
    if 'The Seventh One' in mess:
        mess.remove('The Seventh One')
    if 'Toto XX' in mess:
        mess.remove('Toto XX')
    if 'Falling in Between' in mess:
        mess.remove('Falling in Between')
    if '35th Anniversary - Live in Poland' in mess:
        mess.remove('35th Anniversary - Live in Poland')
    if 'Toto XIV' in mess:
        mess.remove('Toto XIV')
    if 'Old is New' in mess:
        mess.remove('Old is New')
    if '40 Tours Around The Sun - Live in Holland' in mess:
        mess.remove('40 Tours Around The Sun - Live in Holland')
    return mess
