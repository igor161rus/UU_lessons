def all_variants(in_str):
    lst_str = sorted(in_str)
    sort_str = ''.join(lst_str)
    # for i in range(len(sort_str)):
    #     for j in range(i + 1, len(sort_str) + 1):
    #         # print(f'in_str[{i}: {j}] - ', sort_str[i: j])
    #         print(sort_str[i:j])

    res = sorted([sort_str[i: j] for i in range(len(sort_str)) for j in range(i + 1, len(sort_str) + 1)], key=len)
    # print(sorted(res, key=len))
    for i in res:
        yield i


# all_variants("abcfed")

a = all_variants("acb")
for i in a:
    print(i)

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_009\04_hw_v2.py
# a
# b
# c
# ab
# bc
# abc