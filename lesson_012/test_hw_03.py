import unittest

from hw_03 import ExternalResourceGetter

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
        result = getter.run()
        self.assertEqual(result, 535)


if __name__ == '__main__':
    unittest.main()
