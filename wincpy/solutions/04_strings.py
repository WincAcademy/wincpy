ruud = 'Ruud Gullit'
marco = 'Marco van Basten'

goal1 = 35
goal2 = 54

scoorders = ruud + ', ' + marco
print(scoorders)

report = f'{ruud} scoorde in de {goal1}e minuut.\n{marco} scoorde in de {goal2}e minuut.'
print(report)

player = 'Hans van Breukelen'
firstname = player[player.find(' ') + 1:] + ', ' + player[:player.find(' ')]
print(firstname)
lastname_len = len(player[player.find(' ') + 1:])
print(lastname_len)
name_short = player[0] + player[player.find(' '):]
print(name_short)
chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')]))[:-1]
print(chant)
print(chant[-1] == ' ')
