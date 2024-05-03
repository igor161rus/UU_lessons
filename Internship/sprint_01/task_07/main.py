import os

import data_download as dd
import data_plotting as dplt
import calculation as clc
import log

# import logging.config
# from log_settings import log_config
#
# logging.config.dictConfig(log_config)
# logger = logging.getLogger('Logger')


def main():

    log.log_i.info(f'os: {os.name}')
    log.log_i.info(os.getcwd())
    log.log_i.info(os.listdir(os.getcwd()))

    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    period = ''
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    date_start = input("Введите дату начала периода в формате YYYY-MM-DD (для периода по умолчанию, нажмите Enter): ")
    date_end = input(
        "Введите дату окончания периода в формате YYYY-MM-DD (для текущей даты или периода по умолчанию, нажмите Enter): ")
    if date_start == '' or date_end == '':
        period = input(
            "Введите период для данных (например, '1mo' для одного месяца или 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max): ")
    try:
        threshold = float(input("Введите порог для уведомления: "))
    except ValueError:
        threshold = 0

    log.log_i.info(f'period: {period}')
    log.log_i.info(f'ticker: {ticker}')
    log.log_i.info(f'date_start: {date_start}')
    log.log_i.info(f'date_end: {date_end}')
    log.log_i.info(f'threshold: {threshold}')

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker.upper(), period, date_start, date_end)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)
    log.log_i.info(f'Добавлены средние значения (Moving_Average)(шт): {len(stock_data["Moving_Average"])}')

    # Calculate the relative strength (RSI)
    dd.calculate_rsi(stock_data)
    log.log_i.info(f'Добавлены значения RSI (шт): {len(stock_data["RSI"])}')

    # Calculate the standard deviation
    clc.calculation_std(stock_data)
    log.log_i.info(f'Расчитано стандартное отклонение.')

    # Choose the style
    style = dplt.select_styles()
    log.log_i.info(f'Стиль графика: {style}')

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, style)
    log.log_i.info('Сохранен график')

    # Calculate the indicators
    clc.calculate_and_display_average_price(stock_data)
    log.log_i.info('Расчитана средняя цена (AveragePrice)')

    # Notify if strong fluctuations
    clc.notify_if_strong_fluctuations(stock_data, threshold)
    log.log_i.info(f'Уведомления по уровню: {threshold}')

    # Export data to CSV
    filename = input("Введите имя файла для экспорта (например, 'data.csv'), или нажмите Enter для пропуска: ")
    if filename != '':
        clc.export_data_to_csv(stock_data, filename)
        log.log_i.info(f'Экспорт в CSV: {filename}')


if __name__ == "__main__":
    main()
