import unittest
from unittest.mock import patch
import mastermind
import sys
import io
from io import StringIO
from mastermind import *

class TestMastermind(unittest.TestCase):

    def test_create_code(self):
        """
            Checks if the function create_code picks 4 random numbers, starting from 1 till 8
        """

        for i in range (100):
            self.assertNotIn(0, mastermind.create_code())
            self.assertNotIn(9, mastermind.create_code())
            self.assertEqual(len(mastermind.create_code()),4)

    def test_check_correctness(self):
        """
        Checks if the user for the code right. If its wrong the user has 12 turns, if its right it
        displays 'Congratulations! You are a codebreaker!'
        """

        sys.stdout = io.StringIO()
        self.assertTrue(mastermind.check_correctness(6,4))
        self.assertEqual(sys.stdout.getvalue(), 'Congratulations! You are a codebreaker!\n')

        sys.stdout = io.StringIO()
        self.assertFalse(mastermind.check_correctness(5,3))
        self.assertEqual(sys.stdout.getvalue(), 'Turns left: 7\n')

    @patch("sys.stdin", StringIO("123\n12345\n1234\n"))
    def test_input_answer(self):
        """
        Checks if the user put in exactly 4 digits, if they did not it will ask the user
        to put it in again
        """
        
        sys.stdout = io.StringIO()
        self.assertEqual(mastermind.input_answer(),"1234")
        self.assertEqual(sys.stdout.getvalue(),'''Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ''')

    def test_take_turn(self):
        """
        Checks if the 'correct_digits_and_position' and the 'correct_digits_only' is correct
        """

        self.assertEqual(mastermind.take_turn([6,4,2,5], [5,4,2,6]),(2,2))
        self.assertEqual(mastermind.take_turn([5,6,2,3], [5,3,1,6]),(1,2))
        self.assertEqual(mastermind.take_turn([6,5,4,3], [6,5,4,3]),(4,0))

if __name__ == "__main__":
    unittest.main()
