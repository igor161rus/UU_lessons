import time

print(time.gmtime(0))
print(time.time())
print(time.sleep(3))
start = time.monotonic()
huge_number = 2 **100000000
elapsed = time.monotonic() - start
print(f'потрачено {elapsed} секунд')
print('*' * 20, '\n')

import datetime
dt = datetime.date(year=1965, month=7, day=9)
print(f'dt {dt}')

fday = datetime.date.today()

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday())

lunch_time = datetime.time(hour=12, minute=30, second=0, microsecond=5005)
print(f'Время обеда {lunch_time}')
print('*' * 20, '\n')

terminator_day = datetime.datetime(year=1984, month=5, day=12, hour=1,
                                   minute=52, second=00, microsecond=1001)
print(f'Дата терминатора {terminator_day}')
skynet = datetime.datetime(year=1997, month=8, day=29, hour=10, minute=14)
print(f'Дата скайнета {skynet}')

print(skynet.year)
print(skynet.hour)

print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())
print(datetime.datetime.now().timestamp())

print(f'{terminator_day.strftime("%d.%m.%Y")}')
print(f'{terminator_day.strftime("%H:%M:%S")}')
