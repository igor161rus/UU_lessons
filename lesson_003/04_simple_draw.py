from random import random

import simple_draw as sd

length = 200
point = sd.get_point(300, 300)
point_0 = sd.get_point(300, 300)
sd.snowflake(center=point_0, length=200, factor_a=0.5, factor_b=0.3)


# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
#
# v2 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v2.draw()


def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
    v2.draw()

    v2 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
    v2.draw()


# for angle in range(0, 360, 30):
#     triangle(point=point_0, angle=angle)

# x = 100
# y = 500

def fun_snow(n, x, y):
    if n == 1:
        return
    while True:
        x = x * random()
        y = y * random()
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=50)
        y -= 10
        if y < 50:
            break
        # x = x * 1.3
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
    n= n - 1
    fun_snow_x = fun_snow(n, x, y)
    return fun_snow_x

#while True:
sd.clear_screen()
fun_snow(6, 100, 500)
    # point = sd.get_point(x, y)
    # sd.snowflake(center=point, length=50)
    # y -= 10
    # if y < 50:
    #     break
    # x = x * 1.3
    # sd.sleep(0.1)
    # if sd.user_want_exit():
    #     break

sd.pause()
