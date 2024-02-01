import unittest
import asyncio
from main import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('1', 'John Doe', 90, 95)

    def test_calculate_average(self):
        self.assertEqual(self.student.calculate_average(), 92.5)

    def test_get_grade(self):
        self.assertEqual(self.student.get_grade(96), 'A+')
        self.assertEqual(self.student.get_grade(91), 'A')
        self.assertEqual(self.student.get_grade(86), 'B+')
        self.assertEqual(self.student.get_grade(81), 'B')
        self.assertEqual(self.student.get_grade(80), 'C')

    def test_get_remark(self):
        self.assertIn(self.student.get_remark('A+'), ['Great job!', 'Well done!', 'Excellent work!'])
        self.assertIn(self.student.get_remark('B'), ['Keep it up!', 'You are a hardworking student!', 'Good work!'])
        self.assertIn(self.student.get_remark('C'), ['You can do better!', 'Need more effort!', 'Needs improvement!'])

    def test_check_pass_fail(self):
        result = asyncio.run(self.student.check_pass_fail())
        self.assertEqual(result, 'Pass')
        fail_student = Student('2', 'Jane Doe', 30, 40)
        result = asyncio.run(fail_student.check_pass_fail())
        self.assertEqual(result, 'Fail')
        absent_student = Student('3', 'Absent Student', 0, 0)
        result = asyncio.run(absent_student.check_pass_fail())
        self.assertEqual(result, 'Absent')

    def test_get_result(self):
        result = asyncio.run(self.student.get_result())
        self.assertIn('Student Name: John Doe', result)

if __name__ == '__main__':
    unittest.main()