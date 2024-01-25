def all_variants(in_str):
    # j = 0
    # len_str = len(in_str)
    # for i in in_str:
    #     yield i
    # while j < len_str-1:
    #     yield in_str[j] + in_str[j + 1]
    #     j += 1
    # yield in_str

    lst_str = list(sorted(in_str))
    lst_2 = []
    # k = 1
    # len_str = len(lst_str)
    # print(lst_str)
    # for j in lst_str:
    #     if k <= len(lst_str):
    #         for i in lst_str:
    #             k += 1
    #             print(i)
    #
    #     print('jlkj - ', j)
    for i in range(len(in_str)):
        for j in range(i + 1, len(in_str) + 1):
            print(f'in_str[{i}: {j}] - ', in_str[i: j])

    res = sorted([in_str[i: j] for i in range(len(in_str)) for j in range(i + 1, len(in_str) + 1)])
    print(res)

    # for i in lst_str:
    #     print(i)
    #     for n, j in enumerate(lst_str):
    #         end_str = lst_str.pop(0)
    #         print(end_str)
    #         # print(end_str, lst_str[n+1])


all_variants("abс")

# a = all_variants("abc")
# for i in a:
#     print(i)
