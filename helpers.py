import style

def exec_assignment_code(filename):
    """ Execs the code in filename and returns a dictionary with the variables
    in scope minus builtins. """

    with open(filename, 'r') as fp:
        assignment_code = fp.read()

    assignment_state = {}
    print(style.color.gray + 'Output van ' + filename + style.color.end)
    print(style.layout.divider.level_1)
    exec(assignment_code, assignment_state)
    print(style.layout.divider.level_1 + '\n')
    # print(style.color.gray + 'Einde van output\n' + style.color.end)

    del assignment_state['__builtins__']
    return assignment_state
