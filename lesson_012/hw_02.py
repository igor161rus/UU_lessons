# Вам было поручено отобрать сайты которые не работают без VPN (не удаётся подключится),
# а так же те, ответ на запрос к которым не содержит нужно информации (отличных от 200).
#
# Исходный код - https://github.com/yanchuki/RequestsLogger.git
# Не забудьте загрузить зависимости из requierments.txt.
# Простейшая демонстрация работы запроса продемонстрирована в demonstration.py.
#
#
# Все сайты к которым возможно сделать запрос и получить ответ 200 должны записываться в
# отдельный лог-файл (success_responses.log).
# Все сайты к которым возможно сделать запрос и получить ответ отличный от 200 должны записываться в
# отдельный лог-файл (bad_responses.log).
# Все сайты к которым возможно сделать запрос, но получить ответ от них невозможно, должны записываться в
# отдельный лог-файл (blocked_responses.log).
#
# Для того, чтобы узнать у объекта Response код используйте его атрибут status_code.
#
#
# Результат должен получится следующим:
#
# success_responses.log:
# INFO: 'https://www.youtube.com/', response - 200
# INFO: 'https://wikipedia.org', response - 200
# INFO: 'https://yahoo.com', response - 200
# INFO: 'https://yandex.ru', response - 200
# INFO: 'https://whatsapp.com', response - 200
#
# bad_responses.log:
# WARNING: 'https://amazon.com', response - 503
# WARNING: 'https://www.ozon.ru', response - 403
#
# blocked_responses.log:
# ERROR: https://instagram.com, NO CONNECTION
# ERROR: 'https://twitter.com', NO CONNECTION
#
# ПОДСКАЗКА: классы исключений запросов находятся в rq.exceptions. Обрабатывайте их конструкцией try, except.
#
# В отличии от региона проживания ответы могут отличаться.