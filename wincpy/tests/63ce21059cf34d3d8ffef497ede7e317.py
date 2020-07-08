from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'


def run(student_module):
    result = []

    main_abspath = get_main_abspath(student_module)

    assignment_text = open(main_abspath).read()

    requirement = 'De oplossing bevat twee end-of-line comments.'
    end_of_line_comment_count = 0
    for line in assignment_text.split('\n'):
        line = line.replace(' ', '')
        try:
            hash_index = line.index('#')
            if hash_index > 0:
                end_of_line_comment_count += 1
        except ValueError:
            # No comment on this line
            pass
    result.append((requirement, end_of_line_comment_count >= 2))

    requirement = 'De oplossing bevat twee single-line comments.'
    single_line_comment_count = 0
    for line in assignment_text.split('\n'):
        line = line.replace(' ', '')
        if line != '' and line[0] == '#':
            single_line_comment_count += 1
    result.append((requirement, single_line_comment_count >= 2))

    requirement = 'De oplossing bevat twee multiline comments.'
    multiline_comment_count = 0
    for line in assignment_text.split('\n'):
        line = line.replace(' ', '')
        # If we're here we already ran the code, so the multiline comment
        # is also properly terminated somewhere.
        if line != '' and line[0:3] == '"""':
            multiline_comment_count += 1
    result.append((requirement, multiline_comment_count >= 2))

    return result
