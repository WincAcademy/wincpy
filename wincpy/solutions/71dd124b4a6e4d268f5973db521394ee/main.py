ruud = 'Ruud Gullit'
marco = 'Marco van Basten'

goal_0 = 35
goal_1 = 54

scorers = ruud + ' ' + str(goal_0) + ', ' + marco + ' ' + str(goal_1)
print(scorers)

report = f'{ruud} scored in the {goal_0}th minute\n' +\
         f'{marco} scored in the {goal_1}th minute'
print(report)

player = 'Gut von Examplestein'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ') + 1:])
name_short = player[0] + '.' + player[player.find(' '):]
chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')]))[:-1]
good_chant = chant[-1] != ' '

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
