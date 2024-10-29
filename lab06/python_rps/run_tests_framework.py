"""
PLEASE READ CAREFULLY

1. BACKGROUND / SET-UP
----------------------------------------------------------
The unittest module is part of the Python language, and
offers programmers a set of convenience functions and classes 
for organizing and writing tests.

Learn more here: https://docs.python.org/3/library/unittest.html 


2. YOUR TASK
----------------------------------------------------------
Below, a "starter" test class has been defined for you.
It includes two "starter tests" that you can use a model for 
writing your tests. Your job is to implement the remaining tests 
(based on the logic you already figured out from run_tests_vanilla.py).
Note that instead of having your functions return True or False, 
you will now need to use the unittest.TestCase methods. Examples:

    self.assertTrue
    self.assertEqual

List of possible methods described here: 
    https://docs.python.org/3/library/unittest.html 


3. RUNNING THE TESTS
----------------------------------------------------------
To run these tests, issue the following command on the CLI
(from within the python_rps directory):

    python3 run_tests_framework.py --verbose

Good luck!
"""

import unittest

from your_task import hello_world, rps


class TestStringMethods(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello world!")

    def test_paper_beats_rock(self):
        self.assertEqual(rps("rock", "paper"), "Paper wins!")
        self.assertEqual(rps("paper", "rock"), "Paper wins!")

    def test_scissors_beats_paper(self):
        self.assertEqual(rps("paper", "scissors"), "Scissors win!")
        self.assertEqual(rps("scissors", "paper"), "Scissors win!")

    def test_rock_beats_scissors(self):
        self.assertEqual(rps("scissors", "rock"), "Rock wins!")
        self.assertEqual(rps("rock", "scissors"), "Rock wins!")

    def test_tie(self):
        self.assertEqual(rps("rock", "rock"), "It's a tie!")
        self.assertEqual(rps("scissors", "scissors"), "It's a tie!")
        self.assertEqual(rps("paper", "paper"), "It's a tie!")

    # add additional tests below


if __name__ == "__main__":
    unittest.main()
