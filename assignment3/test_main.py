import unittest
from main import Assignment3

class TestAssignment3(unittest.TestCase):

    def test_generate_pascal_triangle(self):
        self.assertEqual(Assignment3.generate_pascal_triangle(0), [])
        self.assertEqual(Assignment3.generate_pascal_triangle(1), [[1]])
        self.assertEqual(Assignment3.generate_pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_generate_prime_numbers(self):
        self.assertEqual(Assignment3.generate_prime_numbers(0), [])
        self.assertEqual(Assignment3.generate_prime_numbers(10), [2, 3, 5, 7])
        self.assertEqual(Assignment3.generate_prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_generate_subsets(self):
        self.assertEqual(Assignment3.generate_subsets(0), [[]])
        self.assertEqual(Assignment3.generate_subsets(1), [[], [1]])
        self.assertEqual(Assignment3.generate_subsets(3), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_int_to_roman(self):
        self.assertEqual(Assignment3.int_to_roman(0), "")
        self.assertEqual(Assignment3.int_to_roman(1), "I")
        self.assertEqual(Assignment3.int_to_roman(9), "IX")
        self.assertEqual(Assignment3.int_to_roman(3999), "MMMCMXCIX")

    def test_calculate_factorial_series(self):
        self.assertEqual(Assignment3.calculate_factorial_series(0), 0)
        self.assertEqual(Assignment3.calculate_factorial_series(1), 1)
        self.assertAlmostEqual(Assignment3.calculate_factorial_series(5), 2.7166666666666663, places=6)

    def test_generate_armstrong_numbers(self):
        self.assertEqual(Assignment3.generate_armstrong_numbers(), [1, 153, 370, 371, 407])

    def test_convert_number(self):
        self.assertEqual(Assignment3.convert_number(0), ('0', '0', '0'))
        self.assertEqual(Assignment3.convert_number(10), ('12', 'a', '1010'))
        self.assertEqual(Assignment3.convert_number(255), ('377', 'ff', '11111111'))

    def test_calculate_natural_logarithm_series(self):
        self.assertEqual(Assignment3.calculate_natural_logarithm_series(2, 0), 0)
        self.assertAlmostEqual(Assignment3.calculate_natural_logarithm_series(2, 5), 0.34657359027997264, places=6)

    def test_calculate_class_average(self):
        self.assertEqual(Assignment3.calculate_class_average([]), (0, False))
        self.assertEqual(Assignment3.calculate_class_average([80, 90, 95]), (88.33333333333333, False))
        self.assertEqual(Assignment3.calculate_class_average([30, 35, 40]), (35, True))

if __name__ == '__main__':
    unittest.main()