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
