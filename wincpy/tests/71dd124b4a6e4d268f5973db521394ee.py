from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)
    expected_state = {
            'goal_0': 35,
            'goal_1': 54,
            'scorers': 'Ruud Gullit 35, Marco van Basten 54',
            'report': 'Ruud Gullit scored in the 35th minute\n' +
                      'Marco van Basten scored in the 54th minute'}

    _, assignment_state = exec_assignment_code(main_abspath)
    result += compare_states(expected_state, assignment_state)

    try:
        player = assignment_state['player']
    except KeyError:
        requirement = 'There is a variable `player`.'
        result.append((requirement, False))
        return result

    expected_state = {
            'first_name': player[:player.find(' ')],
            'last_name_len': len(player[player.find(' ') + 1:]),
            'name_short': player[0] + '.' + player[player.find(' '):],
            'chant': ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')]))[:-1],
            'good_chant': True
            }
    result += compare_states(expected_state, assignment_state)

    return result
