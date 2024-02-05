import unittest
import io
import sys
from patterns import Patterns

class TestPatterns(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def test_rectangle(self):
        Patterns(5).rectangle()
        self.assertEqual(sys.stdout.getvalue().strip(), "\nRectangle Pattern: A rectangle of '*' with height and width of n.\n*****\n*****\n*****\n*****\n*****")

    def test_triangle(self):
        Patterns(5).triangle()
        self.assertEqual(sys.stdout.getvalue().strip(), "\nTriangle Pattern: A right-angled triangle of '*' with height of n.\n*\n**\n***\n****\n*****")

    def test_pyramid(self):
        Patterns(5).pyramid()
        self.assertEqual(sys.stdout.getvalue().strip(), "\nPyramid Pattern: A pyramid of '*' with height of n.\n    *\n   ***\n  *****\n *******\n*********")

    def test_numberPyramid(self):
        Patterns(5).numberPyramid()
        self.assertEqual(sys.stdout.getvalue().strip(), "\nNumber Pyramid Pattern: A pyramid of numbers with height of n.\n    1\n   121\n  12321\n 1234321\n123454321")

    def tearDown(self):
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()