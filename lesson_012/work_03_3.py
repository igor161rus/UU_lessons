import unittest


class MySortTest(unittest.TestCase):

    def test_normal(self):
        result = my_sort([3, 4, 2, 8, 1, 6, 4])
        self.assertEquals(result, [1, 2, 3, 4, 4, 6, 8])

    def test_sorted(self):
        result = my_sort([3, 4, 5])
        self.assertEquals(result, [3, 4, 5], 'text')

    def test_reversed(self):
        result = my_sort([3, 2, 1])
        self.assertEquals(result, [1, 2, 3])

    def test_empty(self):
        result = my_sort([])
        self.assertEquals(result, [])

    def test_with_negative(self):
        result = my_sort([9, 3, -7, 2])
        self.assertEquals(result, [-7, 2, 3, 9])


def my_sort(slist):
    """
    Функция сортировки списков

    >>> my_sort([3,2,1])
    [1, 2, 3]
    """
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i + 1] = slist[i + 1], slist[i]
                was_swap = True
    return slist


if __name__ == '__main__':
    unittest.main()
