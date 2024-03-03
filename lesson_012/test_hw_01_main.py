import unittest
from hw_01_main import Student


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student('Вася')
        self.dict_test = {
            'test_walk_equal': 'Дистанции не равны [дистанция человека({})] != 500',
            'test_walk_greater': 'Дистанция {} меньше 100',
            'test_run_equal': 'Дистанции не равны [дистанция человека({})] != 1000'
        }

    def test_walk_equal(self):
        message = self.dict_test[self.test_walk_equal.__name__]
        for _ in range(10):
            self.student.walk()
        self.assertEqual(self.student.distance, 500, message.format(self.student.name))

    def test_walk_greater(self):
        message = self.dict_test[self.test_walk_greater.__name__]
        for _ in range(10):
            self.student.walk()
        self.assertGreater(self.student.distance, 5, message.format(self.student.name))

    def test_run_equal(self):
        message = self.dict_test[self.test_run_equal.__name__]
        for _ in range(10):
            self.student.run()
        self.assertEqual(self.student.distance, 100, message.format(self.student.name))


if __name__ == '__main__':
    unittest.main()
