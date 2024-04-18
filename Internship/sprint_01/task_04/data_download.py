import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
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
    # Доавляем RSI в DataFrame.
    data['RSI'] = rsi

