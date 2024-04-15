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
    data.to_csv(filename, index=False)