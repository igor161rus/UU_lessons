# try:
#     i = 0
#     print(10 / i)
#     print('ok')
#
# except ZeroDivisionError as esc:
#     print(f'error {esc}')
# except OSError as esc:
#     print(f'error {esc}')


def f1(number):
    return 10 / number


# def f2():
#     summ = 0
#     for i in range(2, -1, -1):
#         try:
#             summ += f1(number=i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(f'внутри f1 что-то пошло не так: {exc}')
#     return summ / 1
#
#
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'внутри f2 что-то пошло не так: {exc}')
#
f = None
try:
    f = open('test.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as exc:
    print('I/O Error', exc)
except ValueError:
    print('no int data')
except Exception as exc:
    print('Error', exc)
else:
    print('read i=', i)
finally:
    if f is not None:
        f.close()


# with open('myfile.txt') as ff:
#     first_line = ff.readline()
# print(first_line)

class InOutBlock:
    def __enter__(self):
        print('Входим в блок кода')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Выходим из блока кода {exc_type}, {exc_val}, {exc_tb}')
        return  True

with InOutBlock() as in_out:
    print('Работаем...')
    a = bla_bla / number
    print('Вычисляем значение')
print('После контекстного менеджера')

