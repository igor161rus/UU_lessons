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


# assert my_sort([3, 4, 2, 8, 1, 6, 4]) == [1, 2, 3, 4, 4, 6, 8], 'что-то не работает'

if __name__ == '__main__':
    import doctest

    doctest.testmod()

