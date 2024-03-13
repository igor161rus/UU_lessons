# python 3.12
import os, fnmatch
import pandas as pd


class PriceMachine:

    def __init__(self):
        self.df = pd.DataFrame(columns=['Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.'])

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
        list_names = ['название', 'продукт', 'товар', 'наименование']
        list_prices = ['розница', 'цена']
        list_weight = ['вес', 'масса', 'фасовка']

        list_files = os.listdir(file_path)
        files = [entry for entry in list_files if fnmatch.fnmatch(entry, pattern)]
        for file in files:
            price = pd.read_csv(file_path + '/' + file)
            for column in price.columns:
                if column in list_names:
                    price = price.rename(columns={column: 'Наименование'})
                elif column in list_prices:
                    price = price.rename(columns={column: 'Цена'})
                elif column in list_weight:
                    price = price.rename(columns={column: 'Вес'})
            price['Файл'] = file
            price['Цена за, кг.'] = (price['Цена'] / price['Вес']).round(1)
            self.df = pd.concat([self.df, price.loc[:, ['Наименование', 'Цена', 'Вес', 'Файл', 'Цена за, кг.']]],
                                axis=0)
            self.df = self.df.sort_values(by=['Цена за, кг.'])
        self.df.index += 1
        self.df.to_csv('output.csv')

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
        self.df = self.df.reset_index()
        self.df.index += 1
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
        return self.df.loc[self.df['Наименование'].str.contains(text)]


pm = PriceMachine()
pm.load_prices('../data')

while True:
    input_text = input('Enter find text, or exit: ')
    if input_text == 'exit':
        break
    else:
        print(pm.find_text(input_text))

print('the end')
with open('file.html', 'wt') as file:
    print(pm.export_to_html(), file=file)
