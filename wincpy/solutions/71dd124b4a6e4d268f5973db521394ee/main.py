# Do not modify these lines
__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"
__human_name__ = "strings"

# Add your code after this line

# Part 1

# 1
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

# 2
goal_0 = 32
goal_1 = 54

# 3
scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)

# 4
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"


# Part 2

# 1
player = "Hennadiy Lytovchenko"

# 2
first_name = player[: player.find(" ")]

# 3
last_name_len = len(player[player.find(" ") :]) - 1

# 4
name_short = f"{player[0]}.{player[player.find(' '):]}"

# 5
chant = f"{first_name}! " * len(first_name)
chant = chant[:-1]

# 6
good_chant = chant[-1] != " "
