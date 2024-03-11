import datetime
import pytz

print(f'Текущая дата, без уточнения тайм-зоны{datetime.datetime.today()}')
print(f'Перечень всех доступных тайм-зон {pytz.all_timezones}')
print(f'В перечне содержится информация о {len(pytz.all_timezones)} тайм-зонах')
print('Asia/Vladivostok' in pytz.all_timezones)
vladyvostok_time_zone = pytz.timezone('Asia/Vladivostok')
moscow_time = datetime.datetime.today()
print(f'Московское время {moscow_time}')
vladyvostok_time = moscow_time.astimezone(vladyvostok_time_zone)
print(f'Владивостокское время {vladyvostok_time}')
print('*' * 20, '\n')

print('Europe/Kaliningrad' in pytz.all_timezones)
kaliningrad_time_zone = pytz.timezone('Europe/Kaliningrad')
UTC_time_zone = pytz.utc

request_from_vladivostok_str = '2019-06-15T16:22:00 +1000'
request_from_kaliningrad_str = '2019-06-15T12:22:00 +0200'

vladyvostok_request = datetime.datetime.strptime(request_from_vladivostok_str, '%Y-%m-%dT%H:%M:%S %z')
kaliningrad_request = datetime.datetime.strptime(request_from_kaliningrad_str, '%Y-%m-%dT%H:%M:%S %z')
print(f'Время отправки запроса по местному времени Владивостока {vladyvostok_request}')
print(f'Время отправки запроса по местному времени Калининграда {kaliningrad_request}')

vladyvostok_request_UTC = vladyvostok_request.astimezone(UTC_time_zone)
kaliningrad_request_UTC = kaliningrad_request.astimezone(UTC_time_zone)
first_request = vladyvostok_request_UTC if kaliningrad_request_UTC > vladyvostok_request_UTC else kaliningrad_request_UTC
print(f'Первый запрос {first_request}')

if vladyvostok_request_UTC > kaliningrad_request_UTC:
    print(f'Первым пришел запрос из Калининграда')
else:
    print(f'Первым пришел запрос из Калининграда')
