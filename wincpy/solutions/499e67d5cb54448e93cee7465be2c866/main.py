# Ignore these lines.
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code below this line.

broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each / 4

num_leeks = 2
num_broccolis = 5
num_potatoes = 7
num_brussel_sprouts = 10

sum_total = num_leeks * leek\
            + num_broccolis * broccoli\
            + num_potatoes * potato\
            + num_brussel_sprouts * brussel_sprout

discount_percentage = 30
discounted_sum_total = sum_total * (1 - discount_percentage / 100)

print(discounted_sum_total)
