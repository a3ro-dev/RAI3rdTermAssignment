class assignment2:
    """
    This class contains methods to solve various programming assignments.
    """
    def __init__(self) -> None:
        print("""Python Programming Lab [Assignment 2]""")

    def printInformation(self, name: str, standard: int, address: str, nationality: str):
        """Question 1: WAPP to print information about yourself."""
        print("User Information:")
        print(f"Name: {name}")
        print(f"Standard: {standard}")
        print(f"Address: {address}")
        print(f"Nationality: {nationality}")

    def numCalc(self, n1: int, n2: int):
        """Question 2: WAPP to perform arithmetic operations on two numbers."""
        print("Addition: ", n1 + n2)
        print("Subtraction: ", n1 - n2)
        print("Multiplication: ", n1 * n2)
        print("Division: ", n1 / n2)

    def calculateGrossSalary(self, basic_salary: float):
        """Question 3: WAPP to calculate gross salary based on basic salary."""
        da = 0.4 * basic_salary  # Calculate dearness allowance
        hra = 0.2 * basic_salary  # Calculate house rent allowance
        gross_salary = basic_salary + da + hra  # Calculate gross salary
        print("Gross Salary: ", gross_salary)

    def convertDistance(self, distance: float):
        """Question 4: WAPP to convert distance from kilometers to meters, feet, inches, and centimeters."""
        meters = distance * 1000  # Convert to meters
        feet = distance * 3280.84  # Convert to feet
        inches = distance * 39370.1  # Convert to inches
        centimeters = distance * 100000  # Convert to centimeters

        print("Distance in Meters: ", meters)
        print("Distance in Feet: ", feet)
        print("Distance in Inches: ", inches)
        print("Distance in Centimeters: ", centimeters)

    def calculateAggregateAndPercentage(self, marks: list):
        """Question 5: WAPP to calculate aggregate marks and percentage marks obtained by a student."""
        total_marks = sum(marks)  # Calculate total marks
        number_of_subjects = len(marks)  # Calculate number of subjects
        maximum_marks = 100  # Maximum marks in each subject

        aggregate_marks = total_marks  # Aggregate marks is the same as total marks
        percentage_marks = (total_marks / (maximum_marks * number_of_subjects)) * 100  # Calculate percentage marks

        print("Aggregate Marks: ", aggregate_marks)
        print("Percentage Marks: ", percentage_marks)

    def convertFahrenheitToCentigrade(self, fahrenheit: float):
        """Question 6: WAPP to convert temperature from Fahrenheit to Centigrade."""
        centigrade = (fahrenheit - 32) * 5/9  # Convert Fahrenheit to Centigrade
        print("Temperature in Centigrade: ", centigrade)

    def calculateRectangleAreaAndPerimeter(self, length: float, breadth: float):
        """Question 7: Calculate the area and perimeter of a rectangle."""
        area = length * breadth
        perimeter = 2 * (length + breadth)
        print("Rectangle Area: ", area)
        print("Rectangle Perimeter: ", perimeter)

    def calculateCircleAreaAndCircumference(self, radius: float):
        """Question 8: Calculate the area and circumference of a circle."""
        import math
        area = math.pi * radius**2
        circumference = 2 * math.pi * radius
        print("Circle Area: ", area)
        print("Circle Circumference: ", circumference)

    def interchangeVariables(self, A, B):
        """Question 9: Interchange the contents of variables A and B."""
        temp = A
        A = B
        B = temp
        print("After interchange:")
        print("A =", A)
        print("B =", B)

    def swapVariables(self, A, B):
        """Question 10: Swap the values of variables A and B without using a third variable."""
        A, B = B, A
        print("After swapping:")
        print("A =", A)
        print("B =", B)

    def calculateTriangleArea(self, base: float, height: float):
        """Question 11: Calculate the area of a triangle given base and height."""
        area = 0.5 * base * height
        print("Triangle Area: ", area)

    def calculatePower(self, base: int, exponent: int):
        """Question 11: Calculate the power of a number given base and exponent."""
        power = base ** exponent
        print("Power: ", power)

    def calculateProduct(self, num1: float, num2: float):
        """Question 12: Calculate the product of two floating point numbers."""
        product = num1 * num2
        print("Product: ", product)

    def printVariableSizes(self):
        """Question 13: Print the size of variables like int, float, etc."""
        import sys
        print("Size of int: ", sys.getsizeof(int()))
        print("Size of float: ", sys.getsizeof(float()))
        # Add more variable types and their sizes as needed

    def calculateQuotientAndRemainder(self, dividend: int, divisor: int):
        """Question 14: Calculate the quotient and remainder in a division."""
        quotient = dividend // divisor
        remainder = dividend % divisor
        print("Quotient: ", quotient)
        print("Remainder: ", remainder)

    def showIncrementAndDecrementResults(self, num: int):
        """Question 15: Show the result of pre-increment, post-increment, pre-decrement, and post-decrement."""
        pre_increment = num + 1
        post_increment = num + 1
        pre_decrement = num - 1
        post_decrement = num - 1
        print("Pre-increment: ", pre_increment)
        print("Post-increment: ", post_increment)
        print("Pre-decrement: ", pre_decrement)
        print("Post-decrement: ", post_decrement)

    def calculateDigitSum(self, number: int):
        """Question 16: Calculate the sum of digits in a five-digit number."""
        digit_sum = sum(int(digit) for digit in str(number))
        print("Digit Sum: ", digit_sum)

    def reverseThreeDigitNumber(self, number: int):
        """Question 17: Reverse a three-digit number."""
        reversed_number = int(str(number)[::-1])
        print("Reversed Number: ", reversed_number)

    def calculateCostPrice(self, selling_price: float, profit: float):
        """Question 18: Calculate the cost price of one item given the total selling price and total profit."""
        number_of_items = 15
        cost_price = (selling_price - profit) / number_of_items
        print("Cost Price of One Item: ", cost_price)

    def calculateFirstAndLastDigitSum(self, number: int):
        """Question 19: Calculate the sum of the first and last digit of a three-digit number."""
        first_digit = int(str(number)[0])
        last_digit = int(str(number)[-1])
        digit_sum = first_digit + last_digit
        print("Sum of First and Last Digit: ", digit_sum)

    def calculateSimpleInterest(self, amount: float, rate: float, years: int):
        """Question 20: Calculate the simple interest given the amount, rate percentage, and years."""
        interest = (amount * rate * years) / 100
        print("Simple Interest: ", interest)

    def solveQuadraticEquation(self, a: float, b: float, c: float):
        """Question 21: Solve a second-order quadratic equation."""
        import math
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print("Root 1: ", root1)
            print("Root 2: ", root2)
        elif discriminant == 0:
            root = -b / (2*a)
            print("Root: ", root)
        else:
            print("No real roots exist.")

def main():
    obj = assignment2()

    print("Which category do you want to access?")
    print("1. Printing specified work")
    print("2. Simple maths")
    print("3. Complicated maths")
    category = int(input())

    if category == 1:
        print("Select a function:")
        print("1. printInformation")
        print("2. printVariableSizes")
        function = int(input())
        if function == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            address = input("Enter address: ")
            nationality = input("Enter nationality: ")
            obj.printInformation(name, age, address, nationality)
        elif function == 2:
            obj.printVariableSizes()

    elif category == 2:
        print("Select a function:")
        print("1. numCalc")
        print("2. calculateRectangleAreaAndPerimeter")
        print("3. calculateTriangleArea")
        print("4. calculateProduct")
        print("5. calculateQuotientAndRemainder")
        function = int(input())
        if function == 1:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            obj.numCalc(num1, num2)
        elif function == 2:
            length = int(input("Enter length: "))
            width = int(input("Enter width: "))
            obj.calculateRectangleAreaAndPerimeter(length, width)
        elif function == 3:
            base = int(input("Enter base: "))
            height = int(input("Enter height: "))
            obj.calculateTriangleArea(base, height)
        elif function == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            obj.calculateProduct(num1, num2)
        elif function == 5:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            obj.calculateQuotientAndRemainder(num1, num2)

    elif category == 3:
        print("Select a function:")
        print("1. calculateGrossSalary")
        print("2. convertDistance")
        print("3. calculateAggregateAndPercentage")
        print("4. convertFahrenheitToCentigrade")
        print("5. calculateCircleAreaAndCircumference")
        print("6. interchangeVariables")
        print("7. swapVariables")
        print("8. calculatePower")
        print("9. calculateDigitSum")
        print("10. reverseThreeDigitNumber")
        print("11. calculateCostPrice")
        print("12. calculateFirstAndLastDigitSum")
        print("13. calculateSimpleInterest")
        print("14. solveQuadraticEquation")
        function = int(input())
        if function == 1:
            basic_salary = float(input("Enter basic salary: "))
            obj.calculateGrossSalary(basic_salary)
        elif function == 2:
            miles = float(input("Enter distance in miles: "))
            obj.convertDistance(miles)
        elif function == 3:
            marks = list(map(int, input("Enter marks separated by space: ").split()))
            obj.calculateAggregateAndPercentage(marks)
        elif function == 4:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            obj.convertFahrenheitToCentigrade(fahrenheit)
        elif function == 5:
            radius = float(input("Enter radius: "))
            obj.calculateCircleAreaAndCircumference(radius)
        elif function == 6:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            obj.interchangeVariables(num1, num2)
        elif function == 7:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            obj.swapVariables(num1, num2)
        elif function == 8:
            base = int(input("Enter base: "))
            exponent = int(input("Enter exponent: "))
            obj.calculatePower(base, exponent)
        elif function == 9:
            num = int(input("Enter a number: "))
            obj.calculateDigitSum(num)
        elif function == 10:
            num = int(input("Enter a three digit number: "))
            obj.reverseThreeDigitNumber(num)
        elif function == 11:
            selling_price = float(input("Enter selling price: "))
            profit = float(input("Enter profit: "))
            obj.calculateCostPrice(selling_price, profit)
        elif function == 12:
            num = int(input("Enter a number: "))
            obj.calculateFirstAndLastDigitSum(num)
        elif function == 13:
            principal = float(input("Enter principal: "))
            rate = float(input("Enter rate: "))
            time = int(input("Enter time: "))
            obj.calculateSimpleInterest(principal, rate, time)
        elif function == 14:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            obj.solveQuadraticEquation(a, b, c)

if __name__ == "__main__":
    main()