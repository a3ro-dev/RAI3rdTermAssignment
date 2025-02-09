import unittest
from main import Assignment3  # replace with the actual module name

class TestAssignment3(unittest.TestCase):
    def test_generate_pascal_triangle(self):
        self.assertEqual(Assignment3.generate_pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_generate_prime_numbers(self):
        self.assertEqual(Assignment3.generate_prime_numbers(10), [2, 3, 5, 7])

    def test_generate_subsets(self):
        self.assertEqual(Assignment3.generate_subsets(2), [(), (1,), (2,), (1, 2)])

    def test_int_to_roman(self):
        self.assertEqual(Assignment3.int_to_roman(4), 'IV')
        self.assertEqual(Assignment3.int_to_roman(9), 'IX')
        self.assertEqual(Assignment3.int_to_roman(58), 'LVIII')
        self.assertEqual(Assignment3.int_to_roman(1994), 'MCMXCIV')

    def test_generate_armstrong_numbers(self):
        self.assertEqual(Assignment3.generate_armstrong_numbers(), [1, 153, 370, 371, 407])

    def test_convert_number(self):
        self.assertEqual(Assignment3.convert_number(10), ('12', 'a', '1010'))

    def test_calculate_class_average(self):
        self.assertEqual(Assignment3.calculate_class_average([50, 60, 70]), (60.0, False))
        self.assertEqual(Assignment3.calculate_class_average([30, 20, 10]), (20.0, True))
    
    def test_calculate_factorial_series(self):
        self.assertAlmostEqual(Assignment3.calculate_factorial_series(5), 2.7166666666666663, places=7)

    def test_calculate_natural_logarithm_series(self):
        import math
        self.assertAlmostEqual(Assignment3.calculate_natural_logarithm_series(2, 5), math.log(2), places=6) # math.log(2) is approximately 0.6931471805599453

if __name__ == '__main__':
    unittest.main()