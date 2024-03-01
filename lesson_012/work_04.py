def my_sort_v1(slist):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i + 1] = slist[i + 1], slist[i]
                was_swap = True
    return slist


def my_sort(slist):
    if len(slist) <= 1:
        return slist
    pivot = slist[0]
    less_then = []
    more_then = []
    # equal = []
    for elem in slist:
        if elem > pivot:
            more_then.append(elem)
        elif elem < pivot:
            less_then.append(elem)
        # else:
        #     equal.append(elem)
    # return my_sort(less_then) + equal + my_sort(more_then)
    return my_sort(less_then) + [pivot, ] + my_sort(more_then)

