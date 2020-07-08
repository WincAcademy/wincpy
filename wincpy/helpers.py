import os
import subprocess
import sys

from wincpy import style


def exec_assignment_code(filename):
    """ Execs the code in filename and returns a dictionary with the variables
    in scope minus builtins. """

    with open(filename, 'r') as fp:
        assignment_code = fp.read()

    state = {}
    print(style.color.gray + 'Output van ' + filename + style.color.end)
    print(style.layout.divider.level_1)
    try:
        exec(assignment_code, state)
    except:
        print(style.color.red
              + 'De code kon niet uitgevoerd worden.\
                \nDebug eerst met de standaard Python interpreter!'
              + style.color.end)
        sys.exit(1)

    print(style.layout.divider.level_1 + '\n')

    del state['__builtins__']

    output = subprocess.run(
        ['python', filename], capture_output=True, text=True
    ).stdout

    return output, state


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
            result.append(
                (f'{style.layout.list_item} Er gaat iets mis bij de variabele {key}.', False))

    return result


def get_main_abspath(module):
    main_abspath = os.path.join(module.__path__[0], 'main.py')
    if not os.path.exists(main_abspath):
        raise FileNotFoundError
    return main_abspath


def get_iddb():
    iddb_url = 'https://raw.githubusercontent.com/WincAcademy/wincid/master/iddb.json'
    iddb_bytes = urllib.request.urlopen(iddb_url, timeout=1).read()
    iddb = json.loads(iddb_bytes)
    try:
        iddb_bytes = urllib.request.urlopen(iddb_url, timeout=1).read()
        iddb = json.loads(iddb_bytes)
    except:
        sys.stderr.write('Could not load database.\n')
        sys.exit(1)
    return iddb
