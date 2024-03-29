# -*- coding: UTF-8 -*-
# python 3.12

import fnmatch
import os
import logging.config
from log_settings import log_config

import pandas as pd

logging.config.dictConfig(log_config)
logger = logging.getLogger('PriceMachineLogger')


class PriceMachine:
    """
    Класс анализатор прайс-листов
    """

    def __init__(self):
        """
            Инициализируется класс с пустым DataFrame, содержащим столбцы
            'Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.'
        """

        self.df = pd.DataFrame(columns=['Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.'])
        self.err = False

    def load_prices(self, file_path=''):
        """
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт

            Допустимые названия для столбца с ценой:
                розница
                цена

            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка

            Args:
                - file_path: Путь к каталогу с csv-файлами.

        """
        pattern = '*price*'
        # Описываются списки с возможными названиями столбцов
        list_names = ['название', 'продукт', 'товар', 'наименование']
        list_prices = ['розница', 'цена']
        list_weight = ['вес', 'масса', 'фасовка']

        # Список всех файлов в каталоге
        # try:
        list_files = os.listdir(file_path)

        log_i = logging.getLogger('info')
        log_e = logging.getLogger('warning')
        log_i.info(f'os: {os.name}')
        log_i.info(os.getcwd())
        log_i.info(os.listdir(os.getcwd()))
        log_i.info(f'pandas version: {pd.__version__}')
        log_i.info(f'Сканируем каталог {file_path}')
        log_i.info(f'В каталоге {file_path} содержится {len(list_files)} файлов')

        # Фильтруем список файлов по шаблону содержащему price
        files = [entry for entry in list_files if fnmatch.fnmatch(entry, pattern)]

        log_i.info(f'Файлы для загрузки {files}')

        if len(files) == 0:
            print('Не найдено файлов для загрузки')
            log_e.warning(f'Не найдено файлов для загрузки')
            self.err = True
            raise FileNotFoundError('Не найдено файлов для загрузки')
        for file in files:
            # Читаем csv-файл
            price = pd.read_csv(file_path + '/' + file, encoding='utf-8')

            log_i.info(f'В файле {file} прочитано {len(price)} строк')
            log_i.info(f'В файле {file} найдены поля {price.columns}')

            # Переименовываем столбцы по спискам
            for column in price.columns:
                if column in list_names:
                    price = price.rename(columns={column: 'Наименование'})
                elif column in list_prices:
                    price = price.rename(columns={column: 'Цена'})
                elif column in list_weight:
                    price = price.rename(columns={column: 'Вес'})

            # Добавляем дополнительные столбцы в исходный DataFrame
            price['Файл'] = file
            price[u'Цена за, кг.'] = (price['Цена'] / price['Вес']).round(1)
            log_i.info(f'Поля из файла {file} после переименования {price.columns}')
            if price.empty:
                # print('Данных не загружено.')
                log_e.warning(f'Из файла {file} данных не загружено')
                self.err = True
                raise FileNotFoundError('Данных не загружено.')

            # Объединяем текущий DataFrame с основным DataFrame self.df.
            # В этом случае получим FutureWarning
            # self.df = pd.concat([self.df, price.loc[:, ['Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.']]],
            #                     axis=0)
            self.df = pd.concat([self.df if not self.df.empty else None,
                                 price.loc[:, ['Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.']]],
                                axis=0)
            log_i.info(f'Из файла {file} загружено  {len(price)} строк')
            # Сортируем DataFrame по столбцу 'Цена за, кг.'
            self.df = self.df.sort_values(by=['Цена за, кг.'])
        log_i.info(f'В DataFrame df загружено {len(self.df)} строк')
        # Нумеруем строки с 1
        self.df['Наименование'] = self.df['Наименование'].str.lower()
        self.df.index += 1
        # self.df.to_csv('output.csv')
        # except FileNotFoundError:
        #     print('Каталог не найден.')
        #     self.err = True
        #     raise FileNotFoundError('Каталог не найден.')

    def export_to_html(self, fname='output.html'):
        """ Функция зкспортируйта DataFrame в таблицу HTML.
        Args:
            - fname(str): Имя выходного HTML - файла.

        :return
            - str: HTML - содержимое, представляющее DataFrame в виде таблицы.
        """

        # Инициализируем содержимое HTML
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>Позиции продуктов</title>
        </head>
        <body>
        <table>
            <tr>
                <th>Номер</th>
                <th>Название</th>
                <th>Цена</th>
                <th>Фасовка</th>
                <th>Файл</th>
                <th>Цена за кг.</th>
            </tr>
        '''
        self.df = self.df.reset_index()
        self.df.index += 1
        # Заполняем строки таблицы значениями DataFrame
        for index, row in self.df.iterrows():
            result += f'''
                <tr>
                    <td>{index}</td>
                    <td>{row['Наименование']}</td>
                    <td>{row['Цена']}</td>
                    <td>{row['Вес']}</td>
                    <td>{row['Файл']}</td>
                    <td>{row['Цена за, кг.']}</td>
                </tr>
            '''
        result += '''
        </table>
        </body>
        </html>
        '''
        return result

    def find_text(self, text):
        """ Функция поиска по содержимому столбца 'Наименование' по заданному тексту.
        Args:
            - text(str): Текст для поиска.
        """
        #  В этом случае возвращаем DataFrame с индексами в файле
        # return self.df.loc[self.df['Наименование'].str.contains(text)]

        # В этом случае возвращаем DataFrame с индексами DataFrame
        # return self.df.loc[self.df['Наименование'].str.contains(text),
        # ['Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.']]

        # Фильтруем DataFrame на основе заданного текста и выбираем определенные столбцы
        search = self.df.loc[self.df['Наименование'].str.contains(text), ['Наименование', 'Цена', 'Вес', 'Файл',
                                                                          'Цена за, кг.']]
        search.reset_index(inplace=True, drop=True)  # Сброс индекса и удаление предыдущего индекса
        # search.index += 1  # Увеличиваем индекс на 1

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        # Нумеруем строки с 1
        search.index += 1

        # Выводим DataFrame
        if not search.empty:
            return search
        else:
            return 'Ничего не найдено.'


pm = PriceMachine()
try:
    pm.load_prices(file_path='../data')
    # pm.load_prices(file_path='.')

    with open('file.html', 'wt', encoding='utf-8') as file:
        print(pm.export_to_html(), file=file)

    while True:
        input_text = input('Enter find text, or exit: ')
        if input_text == 'exit':
            break
        else:
            print(pm.find_text(input_text.lower()))
except FileNotFoundError:
    print('Каталог не найден.')

print('the end')

# В файлах замечены ошибки:
# Enter find text, or exit: Сазан
#     Наименование  Цена  Вес         Файл  Цена за, кг.
# 1  Сазан с кожей   844    4  price_0.csv         211.0
# 2  Сазан с кожей   224    1  price_6.csv         224.0
# 3  Сазан с кожей   242    1  price_7.csv         242.0
# 4  Сазан с кожей   982    4  price_3.csv         245.5
# 5  Сазан с кожей   491    2  price_4.csv         245.5
# Enter find text, or exit: Сзан
#   Наименование  Цена  Вес         Файл  Цена за, кг.
# 1         Сзан   332    2  price_7.csv         166.0
# 2         Сзан   357    2  price_5.csv         178.5
# 3         Сзан   361    2  price_6.csv         180.5
# 4         Сзан   561    3  price_3.csv         187.0
# 5         Сзан   191    1  price_0.csv         191.0
# Enter find text, or exit:
