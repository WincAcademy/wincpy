# Don't modify these variables
__winc_id__ = "f82d22e9845f4b0ea8ff1e3fa6f33a7d"
__human_name__ = "bouncer"

# Add your code below this line


def bouncer_bot(
    is_ladies_night, is_woman, is_full, is_drunk, age, is_wearing_cool_clothes
):
    # Add your code below! #

    return "Welcome!"


# Different combinations of arguments to test all the conditions

# Test 1: Too young
bouncer_bot(False, False, False, False, 17, False)
# Expected output: You're too young. Please come back when you're older.

# Test 2: Too drunk
bouncer_bot(False, False, False, True, 25, False)
# Expected output: Please come back when you're sober.

# Test 3: Ladies night
bouncer_bot(True, False, False, False, 25, False)
# Expected output: It's ladies night. Come back another night.

# Test 4: Too busy
bouncer_bot(False, False, True, False, 25, False)
# Expected output: No, too busy right now.

# Test 5: Welcome!
bouncer_bot(False, False, False, False, 25, True)
# Expected output: Welcome!
