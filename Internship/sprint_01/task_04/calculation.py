def calculate_and_display_average_price(data):
    """
       Вычисляет и выводит среднюю цену по колонке 'Close' в DataFrame.
       Args:
           data (DataFrame): Входные данные содержащие колонку 'Close'.
       Returns:
           None
    """
    # data.to_csv('data.csv', index=False) #для проверки, что там вообще есть
    # https://finance.yahoo.com/quote/AAPL/history?period1=1709942400&period2=1712620800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true
    average_price = data['Close'].mean()
    print(f'Средняя цена: {average_price:.2f} USD')


def notify_if_strong_fluctuations(data, threshold):
    """
       Уведомляет пользователя о сильных колебаниях в цене акции.
       Args:
       - data: DataFrame, содержит данные о цене акции.
       - threshold: float, процентный порог колебаний. Задает максимальное значение процентного изменения цены.
       Returns:
       - None
       """
    # Вычисляем максимальную и минимальную цены.
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    # Вычисляем процентное изменение цены.
    percent_change = ((max_price - min_price) / min_price) * 100
    # Проверяем, если процентное изменение цены больше заданного порога.
    if percent_change > threshold:
        print(f'Произошли сильные колебания по цене {percent_change:.2f}%. '
              f'Максимальная цена: {max_price:.2f} USD. Минимальная цена: {min_price:.2f} USD.')

def export_data_to_csv(data, filename):
    """
       Экспортирует полученные данные в CSV файл без включения индекса.
       Args:
           data (pd.DataFrame): DataFrame для экспорта.
           filename (str): Имя создаваемого CSV файла.
       Returns:
           None
    """
    try:
        data.to_csv(filename, index=False)
    except Exception as e:
        print(f'Не удалось экспортировать данные в CSV. Ошибка: {e}')

def calculate_and_display_relative_strength(data):
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
    # Вычисляем скользящие средние.
    ma_up = up.rolling(window=14).mean()
    ma_down = down.rolling(window=14).mean()

    # Вычисляем индекс RSI с простой скользящей средней.
    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    # Доавляем RSI в DataFrame.
    data['RSI'] = rsi
    # print(up, down, ma_up, ma_down)
    # print(rsi)