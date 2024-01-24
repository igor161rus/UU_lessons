animal = 'зайка'


# def stutter(text):
#     return text[:2] + '-' + text
#
#
# print(stutter(animal))


def shutter_factory(n):
    def stutter(text):
        return (text[:2] + '-') * n + text

    return stutter


stutter_2 = shutter_factory(n=2)
print(stutter_2(animal))

stutters = [shutter_factory(n=n) for n in range(1, 4)]
print(stutters)
for func in stutters:
    print(func(animal))
result = [func(animal) for func in stutters]
print(result)

animals = ['мика', 'бибимот', 'агавка', 'папакан', 'колик', 'соловель']
mesh = [func(animal) for animal in animals for func in stutters]
print(mesh)
