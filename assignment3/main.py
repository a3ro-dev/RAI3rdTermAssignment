import math
from itertools import chain, combinations

class Assignment3:
    """
    A class that contains various methods for generating and calculating different mathematical series and numbers.
    """

    @staticmethod
    def generate_pascal_triangle(n):
        """
        Generates a Pascal's triangle of size n.

        Parameters:
        - n (int): The number of rows in the Pascal's triangle.

        Returns:
        - triangle (list): The Pascal's triangle as a list of lists.
        """
        triangle = []
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(row)
        return triangle

    @staticmethod
    def generate_prime_numbers(n):
        """
        Generates a list of prime numbers up to n.

        Parameters:
        - n (int): The upper limit for generating prime numbers.

        Returns:
        - primes (list): The list of prime numbers.
        """
        primes = []
        for num in range(1, n + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
        return primes

    @staticmethod
    def generate_subsets(n):
        """
        Generates all possible subsets of a set of size n.

        Parameters:
        - n (int): The size of the set.

        Returns:
        - subsets (list): The list of subsets.
        """
        elements = list(range(1, n + 1))
        subsets = list(chain(*map(lambda x: combinations(elements, x), range(0, len(elements)+1))))
        return subsets

    @staticmethod
    def int_to_roman(n):
        """
        Converts an integer to a Roman numeral.

        Parameters:
        - n (int): The integer to be converted.

        Returns:
        - res (str): The Roman numeral representation of the integer.
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for i, v in enumerate(values):
            res += (n // v) * numerals[i]
            n %= v
        return res

    @staticmethod
    def calculate_factorial_series(n):
        """
        Calculates the sum of the factorial series up to n.

        Parameters:
        - n (int): The upper limit for the factorial series.

        Returns:
        - series_sum (float): The sum of the factorial series.
        """
        series_sum = sum(i / math.factorial(i) for i in range(1, n + 1))
        return series_sum

    @staticmethod
    def generate_armstrong_numbers():
        """
        Generates a list of Armstrong numbers between 1 and 500.

        Returns:
        - armstrong_numbers (list): The list of Armstrong numbers.
        """
        armstrong_numbers = []
        for num in range(1, 501):
            sum = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            if num == sum:
                armstrong_numbers.append(num)
        return armstrong_numbers

    @staticmethod
    def convert_number(n):
        """
        Converts an integer to its octal, hexadecimal, and binary representations.

        Parameters:
        - n (int): The integer to be converted.

        Returns:
        - octal (str): The octal representation of the integer.
        - hexadecimal (str): The hexadecimal representation of the integer.
        - binary (str): The binary representation of the integer.
        """
        return oct(n)[2:], hex(n)[2:], bin(n)[2:]

    @staticmethod
    def calculate_natural_logarithm_series(x, n):
        """
        Calculates the sum of the natural logarithm series up to n.

        Parameters:
        - x (float): The base of the natural logarithm.
        - n (int): The number of terms in the series.

        Returns:
        - series_sum (float): The sum of the natural logarithm series.
        """
        series_sum = sum(((x - 1) / x) ** i / 2 for i in range(1, n + 1))
        return series_sum

    @staticmethod
    def calculate_class_average(grades):
        """
        Calculates the average grade and checks if it is below 40.

        Parameters:
        - grades (list): The list of grades.

        Returns:
        - average (float): The average grade.
        - below_passing (bool): True if the average grade is below 40, False otherwise.
        """
        average = sum(grades) / len(grades)
        return average, average < 40

def main():
    while True:
        print("1. Generate Pascal Triangle")
        print("2. Generate Prime Numbers")
        print("3. Generate Subsets")
        print("4. Generate Roman Numbers")
        print("5. Calculate Factorial Series")
        print("6. Generate Armstrong Numbers")
        print("7. Convert Number")
        print("8. Calculate Natural Logarithm Series")
        print("9. Calculate Class Average")
        print("10. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("Enter the number of rows: "))
            print(Assignment3.generate_pascal_triangle(n))
        elif choice == 2:
            n = int(input("Enter the upper limit: "))
            print(Assignment3.generate_prime_numbers(n))
        elif choice == 3:
            n = int(input("Enter the number of elements: "))
            print(Assignment3.generate_subsets(n))
        elif choice == 4:
            n = int(input("Enter the upper limit: "))
            print(Assignment3.int_to_roman(n))
        elif choice == 5:
            n = int(input("Enter the number of terms: "))
            print(Assignment3.calculate_factorial_series(n))
        elif choice == 6:
            print(Assignment3.generate_armstrong_numbers())
        elif choice == 7:
            n = int(input("Enter a decimal number: "))
            print(Assignment3.convert_number(n))
        elif choice == 8:
            x = float(input("Enter the value of x: "))
            n = int(input("Enter the number of terms: "))
            print(Assignment3.calculate_natural_logarithm_series(x, n))
        elif choice == 9:
            grades = []
            while True:
                grade = int(input("Enter grade, -1 to end: "))
                if grade == -1:
                    break
                grades.append(grade)
            print(Assignment3.calculate_class_average(grades))
        elif choice == 10:
            break

if __name__ == "__main__":
    main()