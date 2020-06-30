import subprocess
from unittest import TestCase

from helpers import exec_assignment_code

# Hide unittest module's stuff from traceback
__unittest = True


class TestPrint(TestCase):
    filename = '00_print.py'

    def test_output(self):
        process = subprocess.run(
            ['python', self.filename], capture_output=True, text=True
        )
        self.assertNotEqual(process.stdout, '', 'Er wordt niets geprint.')


class TestVariabelen(TestCase):
    filename = '01_variabelen.py'

    @classmethod
    def setUpClass(self):
        assignment_state = exec_assignment_code(self.filename)
        self.types_in_state = [type(var) for var in assignment_state.values()]

    def test_bool_present(self):
        self.assertIn(bool, self.types_in_state,
                      'Er wordt hier geen bool gedeclareerd.')

    def test_str_present(self):
        self.assertIn(str, self.types_in_state,
                      'Er wordt hier geen string gedeclareerd.')

    def test_int_present(self):
        self.assertIn(int, self.types_in_state,
                      'Er wordt hier geen int gedeclareerd.')


class TestRekenen(TestCase):
    filename = '02_rekenen.py'
    expected_state = {
        'prei': 2,
        'aardappel': 3,
        'spruitje': 7,
        'totaal': 12,
        'gemiddelde_prijs': 4.0,
        'aantal_prei': 2,
        'aantal_aardappel': 7,
        'aantal_spruitje': 10,
        'totaal_prijs': 95,
        'korting_percentage': 30,
        'totaal_prijs_met_korting_afgerond': 66.5}

    @classmethod
    def setUpClass(self):
        self.assignment_state = exec_assignment_code(self.filename)

    def test_variable_names(self):
        """ One-by-one way."""
        for var_name in self.expected_state:
            self.assertIn(var_name, self.assignment_state)

        """ One-shot way."""

        """
        expected_var_names = set(self.expected_state)
        actual_var_names = set(self.assignment_state)
        remainder = expected_var_names - actual_var_names
        self.assertEqual(remainder, set(),
                         f'Je hebt geen variabele met de naam/namen: {remainder}')
                         """

    def test_values(self):
        for key, val in self.expected_state.items():
            self.assertEqual(self.assignment_state[key], val,
                             f'Er gaat iets mis bij de variabele {key}')


class TestComments(TestCase):
    filename = '03_comments.py'

    @classmethod
    def setUpClass(self):
        self.assignment_text = open(self.filename).read()
        self.assignment_state = exec_assignment_code(self.filename)

    def test_end_of_line_comments(self):
        end_of_line_comment_count = 0
        for line in self.assignment_text.split('\n'):
            line = line.replace(' ', '')
            try:
                hash_index = line.index('#')
                if hash_index > 0:
                    end_of_line_comment_count += 1
            except ValueError:
                # No comment on this line
                pass
        self.assertGreaterEqual(end_of_line_comment_count, 2,
                                'Deze oplossing bevat nog geen twee end-of-line comments.')

    def test_single_line_comments(self):
        single_line_comment_count = 0
        for line in self.assignment_text.split('\n'):
            line = line.replace(' ', '')
            if line != '' and line[0] == '#':
                single_line_comment_count += 1

        self.assertGreaterEqual(single_line_comment_count, 2,
                                'Deze oplossing bevat nog geen twee single-line comments.')

    def test_multiline_comments(self):
        multiline_comment_count = 0
        for line in self.assignment_text.split('\n'):
            line = line.replace(' ', '')
            # If we're here, we already ran the code, so the multiline comment
            # is also properly terminated somewhere.
            if line != '' and line[0:3] == '"""':
                multiline_comment_count += 1
        self.assertGreaterEqual(multiline_comment_count, 2,
                                'Deze oplossing bevat nog geen twee multiline comments.')
