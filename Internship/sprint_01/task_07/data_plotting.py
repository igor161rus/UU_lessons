import matplotlib.pyplot as plt
import pandas as pd
import log


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
            str_warn = 'Информация о дате отсутствует или не имеет распознаваемого формата.'
            print(str_warn)
            log.log_w.warn(str_warn)
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
    msg = f"График сохранен как {filename}"
    print(msg)
    log.log_i.info(msg)


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
    msg = f"Стиль графика: {plt.style.available[index - 1]}"
    print(msg)
    log.log_i.info(msg)
    return index - 1
