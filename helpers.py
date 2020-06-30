def exec_assignment_code(filename):
    """ Execs the code in filename and returns a dictionary with the variables
    in scope minus builtins. """

    with open(filename, 'r') as fp:
        assignment_code = fp.read()

    assignment_state = {}
    print('            Output            ')
    print('==============================')
    exec(assignment_code, assignment_state)
    print('==============================')
    print('       Einde van output       \n')

    del assignment_state['__builtins__']
    return assignment_state
