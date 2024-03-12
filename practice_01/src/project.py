import os, fnmatch
import json
import pandas as pd


class PriceMachine():

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

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
        """
        pattern = '*price*'
        list_names = ["название", "продукт", "товар", "наименование"]
        df = pd.DataFrame({
            'Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.',
        })

        list_files = os.listdir(file_path)
        files = [entry for entry in list_files if fnmatch.fnmatch(entry, pattern)]
        for file in files:
            price = pd.read_csv(file_path + '/' + file)
            print(list(price.columns))
            for index, column in enumerate(price.columns):
                if column in list_names:
                    # self.name_length = index
                    print(column, index)
                    df['Наименование'] = price[column]
                    print(df)
            # [column for column in df]

            # print(price.head(10), '\n')

    def _search_product_price_weight(self, headers):
        """
            Возвращает номера столбцов
        """

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
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

    def find_text(self, text):
        pass


pm = PriceMachine()
print(pm.load_prices('D:/Python/Projects/UU/lessons/practice_01/data'))

'''
    Логика работы программы
'''
print('the end')
# print(pm.export_to_html())