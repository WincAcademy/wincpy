import os
import sys
import traceback


from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.text import Text
from rich import box

import wincpy

console = Console(width=100)

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
        "empty_check": "There is a check for this exercise/assignment, but it contains no actual check functions.",
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
            "You could retry after updating Wincpy with `wincpy update`.",
        ],
        "exec_failed": [
            "Make sure your code runs OK with with `python` before running `wincpy check`."
        ],
        "iddb_load_fail": ["Check if you have a working internet connection."],
        "module_import_fail": [
            "We got this error: `{{ exception }}`",
            "Does your code work if you run it yourself?",
            "Is there a file called `main.py` in the directory?",
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
        "empty_check": [
            "This is most likely a development error inside Wincpy. Please report it to a teacher."
        ],
    }.items()
}

successes = {
    "assignment_start": "You can now find your starting files in the directory: `{{ assignment_name }}`"
    "\n\n*Have fun!*",
    "solution_available": "You can now find our example solution in the directory: `{{ solution_dir }}`",
}


logo = """\
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
    console.print(logo, justify="center")


def print_version():
    console.print(Markdown("# Version " + wincpy.__version__))


def report_error(case, **relevant_vars):
    # Assemble and report error
    string = __assemble_ui_string(errors[case], relevant_vars)
    console.print(Markdown(string), style="red")

    # Give tips if we have them
    try:
        string = __assemble_ui_string(tips[case], relevant_vars)
        console.print(Markdown(string), style="blue")
    except KeyError:
        pass


def report_neutral(case, **relevant_vars):
    string = __assemble_ui_string(neutrals[case], relevant_vars)
    console.print(Markdown(string), style="blue")


def report_success(case, **relevant_vars):
    string = __assemble_ui_string(successes[case], relevant_vars)
    console.print(Markdown(string), style="green")


def report_check_result(result):
    table = Table(title="Check Result", show_lines=True, width=100, box=box.ROUNDED)
    table.add_column("Pass/Fail", justify="center")
    table.add_column("Requirement")
    table.add_column("Tips")

    for requirement, fail_reason in result:
        if not fail_reason:
            table.add_row("✅", Markdown(requirement, style="green"), "")
            continue
        elif type(fail_reason) is AssertionError:
            tb = traceback.extract_tb(fail_reason.__traceback__, limit=-1)
            if fail_reason.args:
                reason_txt = fail_reason.args[0]
            else:
                reason_txt = Text.assemble(
                    ("AssertionError", "bold red"),
                    (": We expected\n", "blue"),
                    (tb[0].line.replace("assert ", "") + "\n", "white"),
                )
        elif type(fail_reason) is AttributeError:
            fail_reason = str(fail_reason).split(" ")
            reason_txt = Text.assemble(
                ("AttributeError", "bold red"),
                (": The ", "blue"),
                (fail_reason[0], "white"),
                (" ", ""),
                (" ".join(fail_reason[1:-1]), "blue"),
                (" ", ""),
                (fail_reason[-1], "white"),
            )
        elif issubclass(type(fail_reason), Exception):
            reason_txt = Text.assemble(
                (type(fail_reason).__name__, "bold red"),
                (": " + str(fail_reason), "blue"),
            )
        else:
            reason_txt = Text(str(fail_reason))

        if type(reason_txt) is not Text:
            reason_txt = Markdown(reason_txt)

        table.add_row("❌", Markdown(requirement, style="red"), reason_txt)
    console.print(table)


def print_student_output(output):
    console.print("Output From Your Program", style="bold underline")
    console.print(output)
