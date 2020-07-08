from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)
    expected_state = {
            'goal1': 35,
            'goal2': 54,
            'scoorders': 'Ruud Gullit, Marco van Basten',
            'report': 'Ruud Gullit scoorde in de 35e minuut.'
                      + '\nMarco van Basten scoorde in de 54e minuut.'}

    _, assignment_state = exec_assignment_code(main_abspath)
    result += compare_states(expected_state, assignment_state)

    try:
        player = assignment_state['player']
    except KeyError:
        requirement = 'Je hebt een variabele `player`.'
        result.append((requirement, False))
        return result

    expected_state = {
            'firstname': player[player.find(' ') + 1:] + ', ' + player[:player.find(' ')],
            'lastname_len': len(player[player.find(' ') + 1:]),
            'name_short': player[0] + player[player.find(' '):],
            'chant': ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')]))[:-1]
            }
    result += compare_states(expected_state, assignment_state)

    return result
