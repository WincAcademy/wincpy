broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each / 4

num_leek = 2
num_broccoli = 5
num_potato = 7
num_brussel_sprout = 10

sum_total = num_leek * leek\
            + num_broccoli * broccoli\
            + num_potato * potato\
            + num_brussel_sprout * brussel_sprout

discount_percentage = 30
discounted_sum_total = sum_total * (1 - discount_percentage / 100)

print(discounted_sum_total)
