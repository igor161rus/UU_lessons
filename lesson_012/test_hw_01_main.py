import unittest
from hw_01_main import Student


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student('test')

    def test_walk(self):
        for _ in range(10):
            self.student.walk()
        self.assertEqual(self.student.distance, 50,
                         'Дистанции не равны [дистанция человека({})] != 500'.format(self.student.name))

    def test_run(self):
        for _ in range(10):
            self.student.run()
        self.assertEqual(self.student.distance, 100,
                         'Дистанции не равны [дистанция человека({})] != 1000'.format(self.student.name))


if __name__ == '__main__':
    unittest.main()
