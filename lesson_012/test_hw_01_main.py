import unittest
from hw_01_main import Student


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student('Вася')
        self.dict_test = {
            'test_walk_equal': 'Дистанции не равны [дистанция человека({})] != 50',
            'test_walk_greater': 'Дистанция {} больше, 5',
            'test_run_equal': 'Дистанции не равны [дистанция человека({})] != 1000',
            'test_walk_less': 'Дистанция {} меньше 100',
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
# E:\python\Python312\python.exe "E:/Program Files/JetBrains/PyCharm Community Edition 2023.2.1/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --path E:\python\projects\UU_lessons\lesson_012\test_hw_01_main.py
# Testing started at 18:56 ...
# Launching unittests with arguments python -m unittest E:\python\projects\UU_lessons\lesson_012\test_hw_01_main.py in E:\python\projects\UU_lessons\lesson_012
#
#
# Failure
# Traceback (most recent call last):
#   File "E:\python\projects\UU_lessons\lesson_012\test_hw_01_main.py", line 38, in test_run_equal
#     self.assertEqual(self.student.distance, 10, message.format(self.student.name))
# AssertionError: 100 != 10 : Дистанции не равны [дистанция человека(Вася)] != 1000
#
#
#
# Ran 4 tests in 0.005s
#
# FAILED (failures=1)
#
# Process finished with exit code 1

