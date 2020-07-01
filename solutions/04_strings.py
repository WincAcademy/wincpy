ruud = 'Ruud Gullit'
marco = 'Marco van Basten'

goal1 = 35
goal2 = 54

scoorders = ruud + ', ' + marco
print(scoorders)

report = f'{ruud} scoorde in de {goal1}e minuut.\n{marco} scoorde in de {goal2}e minuut.'
print(report)

hans = 'Hans van Breukelen'
voornaam = hans[hans.find(' ') + 1:] + ', ' + hans[:hans.find(' ')]
print(voornaam)
achternaam_len = len(hans[hans.find(' ') + 1:])
print(achternaam_len)
hans_short = hans[0] + hans[hans.find(' '):]
print(hans_short)
chant = ((hans[:hans.find(' ')] + '! ') * len(hans[:hans.find(' ')]))[:-1]
print(chant)
print(chant[-1] == ' ')
