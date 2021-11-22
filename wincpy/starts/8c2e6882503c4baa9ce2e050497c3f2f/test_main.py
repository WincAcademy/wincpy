import io
import os
import subprocess
from subprocess import PIPE
import sys

import main

import pytest


def test_main(capsys):
    # Test on a short snippet first
    sys.stdin = io.StringIO("abcdef")
    sys.argv = ["main.py", "f"]

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "abcde"
    assert captured.err == "1"

    # Test filtering 'a'
    text = open("random.txt", "r").read()

    filtered_text = open("filtered_a.txt").read()
    filtered_count = "342"

    sys.stdin = io.StringIO(text)
    sys.argv = ["main.py", "a"]
    main.main()
    captured = capsys.readouterr()
    assert captured.out == filtered_text
    assert captured.err == filtered_count

    # Test filtering '7'
    filtered_text = open("filtered_7.txt").read()
    filtered_count = "320"

    sys.stdin = io.StringIO(text)
    sys.argv = ["main.py", "7"]
    main.main()
    captured = capsys.readouterr()
    assert captured.out == filtered_text
    assert captured.err == filtered_count
