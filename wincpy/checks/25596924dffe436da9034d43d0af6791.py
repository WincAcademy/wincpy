from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '25596924dffe436da9034d43d0af6791'


def run(student_module):
    result = []

    # Shortr
    f = student_module.farm_action

    requirement = "Case: farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)"
    result.append((requirement,
                   f('sunny', 'day', True, 'pasture', 'spring', False, True)
                   == "take cows to cowshed\n"
                      "milk cows\n"
                      "take cows back to pasture"))

    requirement = "Case: farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)"
    result.append((requirement,
                   f('rainy', 'night', False, 'cowshed', 'winter', False, True)
                   == "wait"))

    requirement = "Case: farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)"
    result.append((requirement,
                   f('rainy', 'night', False, 'cowshed', 'winter', True, True)
                   == "fertilize pasture"))

    requirement = "Case: farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)"
    result.append((requirement,
                   f('windy', 'night', True, 'cowshed', 'winter', True, True)
                   == "milk cows"))

    requirement = "Case: farm_action('bowling', 'night', False, 'cowshed', 'winter', False, True)"
    result.append((requirement,
                   f('bowling', 'night', False, 'cowshed', 'winter', False, True)
                   == 'wait'))

    requirement = "Case: farm_action('sunny', 'night', True, 'cowshed', 'summer', False, True)"
    result.append((requirement,
                   f('sunny', 'night', True, 'cowshed', 'summer', False, True)
                   == 'milk cows'))

    return result
