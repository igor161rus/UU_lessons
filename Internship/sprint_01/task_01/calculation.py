def calculate_and_display_average_price(data):
    """
       Вычисляет и выводит среднюю цену по колонке 'Close' в DataFrame.
       Args:
           data (DataFrame): Входные данные содержащие колонку 'Close'.
       Returns:
           None
    """
    # data.to_csv('data.csv', index=False)
    average_price = data['Close'].mean()
    print(f'Средняя цена: {average_price:.2f} USD')
