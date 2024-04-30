import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, style_index, filename=None):
    plt.style.use(plt.style.available[style_index])
    plt.figure(figsize=(10, 6)).subplots()

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['RSI'].values, label='RSI')
            plt.plot(dates, data['STD_5'].values, label='STD_5')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['RSI'], label='RSI')
        plt.plot(data['Date'], data['STD_5'], label='STD_5')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart_{style_index + 1}.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def select_styles():
    """
        Функция отображает доступные стили графиков и предлагает пользователю выбрать один из них.
        Returns:
        - index (int): Индекс выбранного стиля.
    """
    # Выводим доступные стили графиков
    print("Available plot styles:")

    # Перечисляем и выводим доступные стили графиков.
    print("Доступные стили графиков:")
    for i, style in enumerate(plt.style.available):
        print(f"{i + 1}. {style}")

    # Предлогаем пользователю выбрать стиль графика
    index = int(input("Выберите стиль графика: "))
    print("Стиль графика:", plt.style.available[index - 1])
    return index - 1
