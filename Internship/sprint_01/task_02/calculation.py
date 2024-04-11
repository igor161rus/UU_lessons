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
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    if (min_price / max_price) * 100 > threshold:
        print(f'Произошли сильные колебания по цене {(min_price / max_price * 100):.2f}%. '
              f'Максимальная цена: {max_price:.2f} USD. Минимальная цена: {min_price:.2f} USD.')
