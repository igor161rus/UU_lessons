import unittest
from hw_01_main import Student


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student('Вася')
        self.student_2 = Student('Федя')
        self.dict_test = {
            'test_walk_equal': 'Дистанции не равны [дистанция человека({})] != 50',
            'test_walk_greater': 'Дистанция {} больше, 5',
            'test_run_equal': 'Дистанции не равны [дистанция человека({})] != 1000',
            'test_walk_less': 'Дистанция {} меньше 100',
            'test_walk_greater_2': '[бегущий человек {}] должен преодолеть дистанцию больше, чем [идущий человек {}]'
        }

    def test_walk_equal(self):
        message = self.dict_test[self.test_walk_equal.__name__]
        for _ in range(10):
            self.student.walk()
        self.assertEqual(self.student.distance, 50, message.format(self.student.name))

    def test_walk_greater(self):
        message = self.dict_test[self.test_walk_greater.__name__]
        for _ in range(10):
            self.student.walk()
        self.assertGreater(self.student.distance, 5, message.format(self.student.name))

    def test_walk_greater_2(self):
        message = self.dict_test[self.test_walk_greater_2.__name__]
        for _ in range(10):
            self.student.walk()
            self.student_2.run()
        self.assertGreater(self.student.distance,
                           self.student_2.distance,
                           message.format(self.student_2.name, self.student.name))

    def test_walk_less(self):
        message = self.dict_test[self.test_walk_less.__name__]
        for _ in range(10):
            self.student.walk()
        self.assertLess(self.student.distance, 100, message.format(self.student.name))

    def test_run_equal(self):
        message = self.dict_test[self.test_run_equal.__name__]
        for _ in range(10):
            self.student.run()
        self.assertEqual(self.student.distance, 10, message.format(self.student.name))


if __name__ == '__main__':
    unittest.main()

# Результат
# "D:\Python\Projects\UU\lessons\course project\Scripts\python.exe" "D:/Program Files/JetBrains/PyCharm Community Edition 2023.2.1/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --path D:\Python\Projects\UU\lessons\lesson_012\test_hw_01_main.py
# Testing started at 9:22 ...
# Launching unittests with arguments python -m unittest D:\Python\Projects\UU\lessons\lesson_012\test_hw_01_main.py in D:\Python\Projects\UU\lessons\lesson_012
#
#
#
# Ran 5 tests in 0.004s
#
# FAILED (failures=2)
#
# Failure
# Traceback (most recent call last):
#   File "D:\Python\Projects\UU\lessons\lesson_012\test_hw_01_main.py", line 49, in test_run_equal
#     self.assertEqual(self.student.distance, 10, message.format(self.student.name))
# AssertionError: 100 != 10 : Дистанции не равны [дистанция человека(Вася)] != 1000
#
#
# Failure
# Traceback (most recent call last):
#   File "D:\Python\Projects\UU\lessons\lesson_012\test_hw_01_main.py", line 35, in test_walk_greater_2
#     self.assertGreater(self.student.distance,
# AssertionError: 50 not greater than 100 : [бегущий человек Федя] должен преодолеть дистанцию больше, чем [идущий человек Вася]
#
#
# Process finished with exit code 1

