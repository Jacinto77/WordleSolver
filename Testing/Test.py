import timeit
from timeit import Timer
from classes.WordList import WordList as wl
from classes.Program import Program as prog
import misc.functions as funct
import sys


def test(did_pass):
    """Print results of a test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """Run the suite of tests for code in specified module."""
    test_prog = prog("../wordlists/new_words_alpha.txt")

    test(test_prog.is_command("\\h") == True)
    test(test_prog.is_command("\\q") == True)
    test(test_prog.is_command("\\s") == False)
    test(test_prog.is_command("\\t") == True)


test_suite()
