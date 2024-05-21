from datetime import datetime, timedelta

import yfinance as yf
import log


def fetch_stock_data(ticker, period='1mo', date_start='', date_end=''):
    """
    Извлекает исторические данные по акциям для данного тикера за указанный период.
    В случае если указано начало и конец периода, параметр period не используется.
    Если не указано начало периода, но указан конец периода и период, то date_start расчитывается.
    Если не указан конец периода, но указано начало периода и период, то date_end расчитывается.

    :param ticker: Биржевой тикер
    :param period: Период данных для получения, по умолчанию — 1mo — «1 месяц».
    :param date_start: Дата начала получения данных. По умолчанию – 99лет назад.
        Дата начала загрузки (ГГГГ-ММ-ДД) или _datetime включительно.
        По умолчанию 99 лет назад.
        Например. для start="2020-01-01" первая точка данных будет "2020-01-01"
    :param date_end: Дата окончания получения данных, по умолчанию — сейчас.
        Дата окончания загрузки (ГГГГ-ММ-ДД) или _datetime, не включая.
        По умолчанию сегодняшняя
        Например, для end="2023-01-01" последняя точка данных будет "2022-12-31"
    :return: Исторические данные об акции за указанный период

    """
    # period_list = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    now_year = str(datetime.now().year) + '-01-01'
    if period == 'ytd' and date_end != '':
        day_now_year = datetime.strptime(date_end, "%Y-%m-%d") - datetime.strptime(now_year, "%Y-%m-%d")
    else:
        day_now_year = datetime.now() - datetime.strptime(now_year, "%Y-%m-%d")

    dict_timedelta = {'1d': timedelta(days=1),
                      '5d': timedelta(days=5),
                      '1mo': timedelta(days=30),
                      '3mo': timedelta(days=90),
                      '6mo': timedelta(days=180),
                      '1y': timedelta(days=365),
                      '2y': timedelta(days=730),
                      '5y': timedelta(days=1825),
                      '10y': timedelta(days=3650),
                      'ytd': timedelta(days=day_now_year.days),
                      'max': timedelta(days=36500)}

    # if period not in period_list:
    #     raise ValueError('Период должен быть одним из следующих значений: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max')
    stock = yf.Ticker(ticker)
    # Обработка значений по умолчанию для date_start и date_end
    if date_start == '' or date_start is None:
        if date_end == '' or date_start is None:
            date_start = (datetime.now() - dict_timedelta[period]).strftime("%Y-%m-%d")
        else:
            date_start = (datetime.strptime(date_end, "%Y-%m-%d") - dict_timedelta[period]).strftime("%Y-%m-%d")
    if date_end == '' or date_end is None:
        if period == '' or period is None:
            date_end = datetime.now().strftime("%Y-%m-%d")
        else:
            date_end = (datetime.strptime(date_start, "%Y-%m-%d") + dict_timedelta[period]).strftime("%Y-%m-%d")
    if date_start > date_end:
        raise ValueError('Дата окончания периода должна быть больше даты начала периода')

    data = stock.history(period=period, start=date_start, end=date_end)
    if len(data) > 0:
        log.log_i.info(f'Получено: {len(data)} значений')
    else:
        log.log_i.info('Получено: 0 значений')
        log.log_w.warn('Данных не получено')
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_rsi(data):
    """
       Вычесление индекса (RSI) и добавление его в DataFrame.
       Parameters:
            data (DataFrame): Входные данные содержащие колонку 'Close' цена закрытия.
       Returns:
            None
       """

    # Вычисляем изменение цены.
    close_delta = data['Close'].diff()
    # Разделяем цены на положительные и отрицательные.
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    # Вычисляем скользящие средние (значение 14 рекомендуется).
    ma_up = up.rolling(window=14).mean()
    ma_down = down.rolling(window=14).mean()

    # Вычисляем индекс RSI с простой скользящей средней.
    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    # Добавляем RSI в DataFrame.
    data['RSI'] = rsi
