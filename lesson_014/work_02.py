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
print(f'{terminator_day.strftime("%d.%m.%Y время %H:%M:%S")}')

kd = datetime.datetime.strptime('06.09.2016', '%d.%m.%Y')
print(f'kd {kd}')
print(kd.month)
print(kd.year)

d = datetime.datetime.combine(dt, lunch_time)
print(f'd {d}')

end_skynet = datetime.datetime(year=2029, month=7, day=11)
duration = end_skynet - skynet
print(f'Длительность скайнета {duration.days} дней, {duration.seconds} секунд')
print(type(duration))
print(skynet + duration)
print(duration * 2)
wt = datetime.timedelta(weeks=40, days=11358, hours=13, minutes=36, seconds=600)
print(end_skynet - wt)
print('*' * 20, '\n')

incoming_date = '30-11-2018'
incoming_date_datetime = datetime.datetime.strptime(incoming_date, '%d-%m-%Y')

registration_end_time = datetime.datetime(year=2019, month=1, day=1)
if incoming_date_datetime > registration_end_time:
    print('Вход запрещен')
else:
    print('Вход разрешен')

