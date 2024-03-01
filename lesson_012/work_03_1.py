def my_sort(slist):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i + 1] = slist[i + 1], slist[i]
                was_swap = True
    return slist


print(my_sort([3, 4, 2, 8, 1, 6, 4]))
print(my_sort([3, 4, 5]))
print(my_sort([3, 2, 1]))
print(my_sort([]))
print(my_sort([9, 3, -7, 2]))

if my_sort([3, 4, 2, 8, 1, 6, 4]) != [1, 2, 3, 4, 4, 6, 8]:
    print('Error')
if my_sort([3, 4, 5]) != [3, 4, 5]:
    print('Error!')
if my_sort([3, 2, 1]) != [1, 2, 3]:
    print('Error')
if my_sort([]):
    print('Error!')
if my_sort([9, 3, -7, 2]) != [-7, 2, 3, 9]:
    print('Error!')
