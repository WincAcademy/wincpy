import subprocess
from subprocess import PIPE
import os

import pytest

def test_main():
    # Test on a short snippet first
    stdin = 'abcdef'
    exit_code, result = subprocess.getstatusoutput('echo abcdef | python main.py f')
    assert exit_code == 0 and (result == '1abcde' or result == 'abcde1')

    # Test filtering 'a'
    text = open('random.txt', 'r').read()
    filtered_text = text.replace('a', '')[:-1]
    filtered_count = str(text.count('a'))
    exit_code, result = subprocess.getstatusoutput('cat random.txt | python main.py a')
    assert exit_code == 0 and (result == filtered_count + filtered_text
                               or result == filtered_text + filtered_count)

    # Test filtering '7'
    filtered_text = text.replace('7', '')[:-1]
    filtered_count = str(text.count('7'))
    exit_code, result = subprocess.getstatusoutput('cat random.txt | python main.py 7')
    assert exit_code == 0 and (result == filtered_count + filtered_text
                               or result == filtered_text + filtered_count)
