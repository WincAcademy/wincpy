import sys
import os

from rich.console import Console
from rich.markdown import Markdown

console = Console()

# Constants
errors = {
    k: "**Error:** " + v
    for k, v in {
        "solve_first": "Solve the exercise before viewing Winc's solution.",
        "unknown_winc_id": "Winc ID not recognized.",
        "dir_exists": "Can't create a folder called `{{ dirname }}` in the current directory.",
        "no_check_found": "There is no check for the exercise/assignment `{{ assignment_name }}`.",
        "exec_failed": "Your code could not be executed successfully.",
        "iddb_load_fail": "Can't load Winc ID database.",
        "module_import_fail": "Can't import `{{ module_name }}` from directory: `{{ dir }}`.",
        "module_no_winc_id": "Imported module `{{ module_name }}` from directory: `{{ dir }}`, but it has no Winc ID.",
        "no_solution_available": "There's no solution available for the exercise/assignment {{ exercise_name }}.",
        "check_failed": "Something went wrong while checking your code. Python gave us the following reason:\n> `{{ exception }}`",
    }.items()
}

neutrals = {"assignment_start": "Starting assignment: `{{ assignment_name }}`"}

tips = {
    k: "**Tips:**\n" + "\n".join("- " + s for s in v)
    for k, v in {
        "general": [
            "Check your assumptions; verify that things work the way you think they do by trying them out in a REPL first.",
            "Add print statements (`print(example_variable)`) at different points in your code to check your variables.",
        ],
        "unknown_winc_id": [
            "Double check you copy-pasted the ID correctly.",
            "Update Wincpy with `wincpy update` and retry.",
        ],
        "dir_exists": [
            "Navigate to this folder in Finder (macOS) or Explorer (Windows).",
            "Check if there is a folder named like it, and rename or remove it.",
        ],
        "no_check_found": [
            "It's probably intentional that there is no check for this exercise/assignment.",
            "You could try updating Wincpy by running `wincpy update`.",
        ],
        "exec_failed": [
            "Make sure your code runs OK with with `python` before running `wincpy check`."
        ],
        "iddb_load_fail": ["Check if you have a working internet connection."],
        "module_import_fail": [
            "Check if there is a file called `main.py` in the directory."
        ],
        "module_no_winc_id": [
            "Open `main.py` and check if it has a Winc ID. It should look like this: ```__winc_id__ = '31a...59f'```"
        ],
        "no_solution_available": [
            "It's probably intentional that there is no solution for this exercise/assignment.",
            "You could try updating Wincpy by running `wincpy update`.",
        ],
        "check_failed": [
            "Some of the **variable names** might be different from how they are specified in the assignment.",
            "Some of the **function names** might be different from how they are specified in the assignment.",
            "Your function might not return the correct data type. For example: a string (`'5'`) instead of an `int` (`5`).",
            "You haven't finished implementing the assignment yet, so a function or attribute is still missing.",
        ],
    }.items()
}

successes = {
    "assignment_start": "You can now find your starting files in the directory: `{{ assignment_name }}`"
    "\n\n*Have fun!*",
    "solution_available": "You can now find our example solution in the directory: `{{ solution_dir }}`",
}


logo = """
█░█░█ █ █▄░█ █▀▀ █▀█ █▄█
▀▄▀▄▀ █ █░▀█ █▄▄ █▀▀ ░█░\n"""


__original_stdout = sys.stdout


def __assemble_ui_string(string, relevant_vars):
    for k, v in relevant_vars.items():
        string = string.replace("{{ " + k + " }}", v)
    return string


def mute_stdout():
    sys.stdout = open(os.devnull, "w")


def unmute_stdout():
    sys.stdout.close()
    sys.stdout = __original_stdout


def print_intro():
    console.print(logo, justify="left")


def report_error(case, **relevant_vars):
    # Assemble and report error
    string = __assemble_ui_string(errors[case], relevant_vars)
    console.print(Markdown(string), style="red")

    # Give tips if we have them
    try:
        console.print(Markdown(tips[case]), style="blue")
    except KeyError:
        pass


def report_neutral(case, **relevant_vars):
    string = __assemble_ui_string(neutrals[case], relevant_vars)
    console.print(Markdown(string), style="blue")


def report_success(case, **relevant_vars):
    string = __assemble_ui_string(successes[case], relevant_vars)
    console.print(Markdown(string), style="green")


def report_check_result(result):
    console.print("Check Result", style="bold underline")
    for requirement, score in result:
        if score:
            console.print(Markdown("- 👍 " + requirement), style="green")
        else:
            console.print(Markdown("- 👎 " + requirement), style="red")


def print_student_output(output):
    console.print("Output From Your Program", style="bold underline")
    console.print(output)
