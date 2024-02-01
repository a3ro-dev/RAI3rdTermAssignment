# The provided Python code defines a `Student` class with attributes `roll_no`, `name`, `theory_marks`, and `practical_marks`. The class also has several methods:

# - `calculate_average()`: Calculates the average of theory and practical marks.
# - `get_grade(average: float)`: Determines the grade based on the average marks.
# - `get_remark()`: Returns a random remark from a list of remarks.
# - `check_pass_fail()`: Checks if the student has passed or failed based on the marks.
# - `get_result()`: Returns the final result of the student.

# The `__init__` method is the constructor that initializes the instance variables when a new object of the `Student` class is created. 

import asyncio
import random

class Student:
    """
    A class to represent a student.

    ...

    Attributes
    ----------
    roll_no : str
        a formatted string of roll number assigned to a student
    name : str
        a formatted string of student's name
    theory_marks : int
        an integer representing marks obtained in theory
    practical_marks : int
        an integer representing marks obtained in practical

    Methods
    -------
    calculate_average():
        Returns the average of theory and practical marks.
    get_grade(average: float):
        Returns the grade based on the average marks.
    get_remark():
        Returns a random remark from a list of remarks.
    check_pass_fail():
        Checks if the student has passed or failed based on the marks.
    get_result():
        Returns the final result of the student.
    """

    def __init__(self, roll_no, name, theory_marks, practical_marks):
        """Constructs all the necessary attributes for the student object."""

        self.roll_no = roll_no
        self.name = name
        self.theory_marks = theory_marks
        self.practical_marks = practical_marks

    def calculate_average(self):
        """Returns the average of theory and practical marks."""

        return (self.theory_marks + self.practical_marks) / 2

    def get_grade(self, average):
        """Returns the grade based on the average marks."""

        if average > 95:
            return 'A+'
        elif average > 90:
            return 'A'
        elif average > 85:
            return 'B+'
        elif average > 80:
            return 'B'
        else:
            return 'C'

    def get_remark(self, grade):
        """Returns a remark based on the student's grade."""

        if grade in ['A+', 'A']:
            remarks = ['Great job!', 'Well done!', 'Excellent work!']
        elif grade in ['B+', 'B']:
            remarks = ['Keep it up!', 'You are a hardworking student!', 'Good work!']
        else:
            remarks = ['You can do better!', 'Need more effort!', 'Needs improvement!']

        return random.choice(remarks)

    async def check_pass_fail(self):
        """Checks if the student has passed or failed based on the marks."""

        if self.theory_marks == 0:
            return 'Absent'
        elif self.theory_marks < 35: # or self.practical_marks < 35:
            return 'Fail'
        else:
            average = self.calculate_average()
            if average <= 35:
                return 'Fail'
            else:
                return 'Pass'
            
    async def loading_animation(self):
        frames = ["/", "-", "\\", "|"]
        i = 0
        while i < 5:
            print(f"Calculating result... {frames[i % 4]}")
            await asyncio.sleep(1)
            i += 1

    async def get_result(self):
        """Returns the final result of the student."""

        await self.loading_animation()

        result = await self.check_pass_fail()
        if result == 'Pass':
            average = self.calculate_average()
            grade = self.get_grade(average)
            remark = self.get_remark(grade)
            return f"\n----------------------------------------\n" \
                f"Student Name: {self.name}\n" \
                f"Roll Number: {self.roll_no}\n" \
                f"Grade: {grade}\n" \
                f"Remark: {remark}\n" \
                f"----------------------------------------\n"
        elif result == 'Fail':
            return f"\n----------------------------------------\n" \
                f"Student Name: {self.name}\n" \
                f"Roll Number: {self.roll_no}\n" \
                f"Status: Failed\n" \
                f"----------------------------------------\n"
        else:
            return f"\n----------------------------------------\n" \
                f"Student Name: {self.name}\n" \
                f"Roll Number: {self.roll_no}\n" \
                f"Status: Absent\n" \
                f"----------------------------------------\n"
        
def main():
    """Main function to execute the program."""

    try:
        roll_no = input('Enter Roll No: ')
        name = input('Enter Name: ')
        theory_marks = int(input('Enter Theory Marks: '))
        practical_marks = int(input('Enter Practical Marks: '))
        student = Student(roll_no, name, theory_marks, practical_marks)
    except ValueError as e:
        print("Invalid input. Please enter a valid number for marks.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(student.get_result())
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()