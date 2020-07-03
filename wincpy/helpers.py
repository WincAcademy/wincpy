from wincpy import style


def exec_assignment_code(filename):
    """ Execs the code in filename and returns a dictionary with the variables
    in scope minus builtins. """

    with open(filename, 'r') as fp:
        assignment_code = fp.read()

    actual_state = {}
    print(style.color.gray + 'Output van ' + filename + style.color.end)
    print(style.layout.divider.level_1)
    exec(assignment_code, actual_state)
    print(style.layout.divider.level_1 + '\n')

    del actual_state['__builtins__']
    return actual_state


def compare_states(expected_state, actual_state):
    """
    Takes two dicts of {var_name: var_value} and results a list of tuples
    (requirement, True/False) that represents how the two states compare.
    """

    result = []

    requirement = 'Alle variabelen zijn goed gedeclareerd.'
    expected_var_names = set(expected_state)
    actual_var_names = set(actual_state)
    remainder = expected_var_names - actual_var_names
    result.append((requirement, len(remainder) == 0))
    if remainder is not None:
        for key in remainder:
            result.append(
                (f'--> Er gaat iets mis bij de variabele {key}.', False))

    requirement = 'Alle variabelen bevatten de juiste waarden.'
    es_tupleset = set(expected_state.items())
    as_tupleset = set(actual_state.items())
    result.append((requirement, es_tupleset <= as_tupleset))
    if not result[-1][1]:
        diff = es_tupleset - as_tupleset
        for key, _ in diff:
            result.append((f'{style.layout.list_item} Er gaat iets mis bij de variabele {key}.', False))

    return result
