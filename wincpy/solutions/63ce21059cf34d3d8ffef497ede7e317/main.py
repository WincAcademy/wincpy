broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7 # Expensive!

sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each / 4 # Glad I could reuse sum_one_each here.

num_leek = 2
num_broccoli = 5
num_potato = 7
num_brussel_sprout = 10

"""This is a big one. I need multiple lines to explain this.
Fortunately I have this multiline comment.

"\" at the end of a line tells Python to continue reading this instruction
on the next line.
"""

sum_total = num_leek * leek\
            + num_broccoli * broccoli\
            + num_potato * potato\
            + num_brussel_sprout * brussel_sprout

# Thanks for that discount.
discount_percentage = 30
discounted_sum_total = sum_total * (1 - discount_percentage / 100)

""" We're almost done! """
print(discounted_sum_total)

# Done!
