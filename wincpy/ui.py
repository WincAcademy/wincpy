from rich.console import Console
from rich.markdown import Markdown

console = Console(width=80)

# Constants
errors = {
    k: '**Error:** ' + v for k, v in
    {
        'solve_first': "Solve the exercise before viewing Winc's solution.",
        'unknown_winc_id': "Winc ID not recognized.",
        'dir_exists': "Can't create a folder called `{{ dirname }}` in the current directory.",
        'no_check_found': 'There is no check for the exercise/assignment `{{ assignment_name }}`.'
    }.items()
}

neutrals = {
    'assignment_start': 'Starting assignment: `{{ assignment_name }}`'
}

tips = {
    k: '**Tips:**\n' + '\n'.join('- ' + s for s in v) for k, v in
    {
        'unknown_winc_id':
            ['Double check you copy-pasted the ID correctly.',
             'Update Wincpy with `wincpy update` and retry.'],
        'dir_exists':
            ['Navigate to this folder in Finder (macOS) or Explorer (Windows).',
             'Check if there is a folder named like it, and rename or remove it.'],
        'no_check_found':
            ["It's probably intentional that there is no check for this exercise/assignment.",
             'You could try updating Wincpy by running `wincpy update`.']
    }.items()
}

successes = {
    'assignment_start': 'You can now find your starting files in the directory: `{{ assignment_name }}`'
                        '\n\n*Have fun!*',
}


def __assemble_ui_string(string, relevant_vars):
    for k, v in relevant_vars.items():
        string = string.replace('{{ ' + k + ' }}', v)
    return string


def report_error(case, **relevant_vars):
    # Assemble and report error
    string = __assemble_ui_string(errors[case], relevant_vars)
    console.print(Markdown(string), style='red')

    # Give tips if we have them
    try:
        console.print(Markdown(tips[case]), style='blue')
    except KeyError:
        pass


def report_neutral(case, **relevant_vars):
    string = __assemble_ui_string(neutrals[case], relevant_vars)
    console.print(Markdown(string), style='blue')


def report_success(case, **relevant_vars):
    string = __assemble_ui_string(successes[case], relevant_vars)
    console.print(Markdown(string), style='green')

