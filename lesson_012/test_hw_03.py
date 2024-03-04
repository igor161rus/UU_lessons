import unittest

from hw_03 import ExternalResourceGetter
from lesson_012 import hw_03

_test_data = """
1234567
12345
123456789
12
"""


class FakeResult:
    def __init__(self):
        self.text = _test_data


def fake_get_result(*args, **kwargs):
    return FakeResult()


class ExternalResourceGetterTest(unittest.TestCase):
    def test_normal(self):
        getter = ExternalResourceGetter(url='https://www.python.org')
        hw_03.requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
