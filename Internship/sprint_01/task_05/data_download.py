from datetime import datetime, timedelta

import yfinance as yf


def fetch_stock_data(ticker, period='1mo', date_start=None, date_end=None):
    """
    Извлекает исторические данные по акциям для данного тикера за указанный период.
    В случае если указано начало и конец периода, параметр period не используется.
    Если не указано начало периода, но указан конец периода и период, то date_start расчитывается.
    Если не указан конец периода, но указано начало периода и период, то date_end расчитывается.

    :param ticker: Биржевой тикер
    :param period: Период данных для получения, по умолчанию — 1mo — «1 месяц».
    :param date_start: Start date for data retrieval, default is 99 years ago
        Дата начала загрузки (ГГГГ-ММ-ДД) или _datetime включительно.
        По умолчанию 99 лет назад.
        Например. для start="2020-01-01" первая точка данных будет "2020-01-01"
    :param date_end: End date for data retrieval, default is now
        Дата окончания загрузки (ГГГГ-ММ-ДД) или _datetime, не включая.
        По умолчанию сегодняшняя
        Например, для end="2023-01-01" последняя точка данных будет "2022-12-31"
    :return: Исторические данные об акции за указанный период

    """
    # period_list = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    dict_timedelta = {'1d': timedelta(days=1),
                      '5d': timedelta(days=5),
                      '1mo': timedelta(days=30),
                      '3mo': timedelta(days=90),
                      '6mo': timedelta(days=180),
                      '1y': timedelta(days=365),
                      '2y': timedelta(days=730),
                      '5y': timedelta(days=1825),
                      '10y': timedelta(days=3650),
                      'ytd': timedelta(days=365),
                      'max': timedelta(days=0)}

    # if period not in period_list:
    #     raise ValueError('Период должен быть одним из следующих значений: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max')
    stock = yf.Ticker(ticker)
    # Обработка значений по умолчанию для date_start и date_end
    if date_start == '':
        if date_end == '':
            date_start = (datetime.now() - dict_timedelta[period]).strftime("%Y-%m-%d")
        else:
            date_start = (datetime.strptime(date_end, "%Y-%m-%d") - dict_timedelta[period]).strftime("%Y-%m-%d")
    if date_end == '':
        if period == '':
            date_end = datetime.now().strftime("%Y-%m-%d")
        else:
            date_end = (datetime.strptime(date_start, "%Y-%m-%d") + dict_timedelta[period]).strftime("%Y-%m-%d")
    if date_start > date_end:
        raise ValueError('Дата окончания периода должна быть больше даты начала периода')

    data = stock.history(period=period, start=date_start, end=date_end)
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
