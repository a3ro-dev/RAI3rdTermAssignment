import unittest
from main import assignment2

class TestAssignment2(unittest.TestCase):
    def setUp(self):
        self.assignment = assignment2()

    def test_printInformation(self):
        self.assignment.printInformation("John Doe", 10, "123 Main St", "American")

    def test_numCalc(self):
        self.assignment.numCalc(10, 5)

    def test_calculateGrossSalary(self):
        self.assignment.calculateGrossSalary(1000)

    def test_convertDistance(self):
        self.assignment.convertDistance(10)

    def test_calculateAggregateAndPercentage(self):
        self.assignment.calculateAggregateAndPercentage([90, 80, 70, 60, 50])

    def test_convertFahrenheitToCentigrade(self):
        self.assignment.convertFahrenheitToCentigrade(32)

    def test_calculateRectangleAreaAndPerimeter(self):
        self.assignment.calculateRectangleAreaAndPerimeter(10, 5)

    def test_calculateCircleAreaAndCircumference(self):
        self.assignment.calculateCircleAreaAndCircumference(10)

    def test_interchangeVariables(self):
        self.assignment.interchangeVariables(10, 5)

    def test_swapVariables(self):
        self.assignment.swapVariables(10, 5)

    def test_calculateTriangleArea(self):
        self.assignment.calculateTriangleArea(10, 5)

if __name__ == '__main__':
    unittest.main()