# Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и
# уходящих после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и
# уходят. Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
#
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола, is_busy(bool) -
# занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов,
# в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае -
# посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)
#
# Пример работы:
# # Создаем столики в кафе
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(3)
# tables = [table1, table2, table3]
#
# # Инициализируем кафе
# cafe = Cafe(tables)
#
# # Запускаем поток для прибытия посетителей
# customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
# customer_arrival_thread.start()
#
# # Ожидаем завершения работы прибытия посетителей
# customer_arrival_thread.join()
#
# Вывод на консоль (20 посетителей [ограничение выставить в методе customer_arrival]):
# Посетитель номер 1 прибыл
# Посетитель номер 1 сел за стол 1
# Посетитель номер 2 прибыл
# Посетитель номер 2 сел за стол 2
# Посетитель номер 3 прибыл
# Посетитель номер 3 сел за стол 3
# Посетитель номер 4 прибыл
# Посетитель номер 4 ожидает свободный стол
# Посетитель номер 5 прибыл
# Посетитель номер 5 ожидает свободный стол
# ......
# Посетитель номер 20 прибыл
# Посетитель номер 20 ожидает свободный стол
# Посетитель номер 17 покушал и ушёл.
# Посетитель номер 20 сел за стол N.
# Посетитель номер 18 покушал и ушёл.
# Посетитель номер 19 покушал и ушёл.
# Посетитель номер 20 покушал и ушёл.
from datetime import time
from threading import Thread
from time import sleep
import queue


class Table(Thread):
    def __init__(self, number, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)
        self.number = number
        self.is_busy = False


class Cafe(Thread):
    """класс для симуляции процессов в кафе"""

    def __init__(self, tables, *args, **kwargs):
        super(Cafe, self).__init__(*args, **kwargs)
        self.queue = 0
        self.tables = tables
        self.customer = 0
        self.table_status = []

    def customer_arrival(self):
        """моделирует приход посетителя(каждую секунду)."""
        sleep(1)
        self.customer += 1
        print(f'Посетитель номер {self.customer} прибыл', flush=True)
        self.serve_customer(self.customer)

    def serve_customer(self, customer):
        """моделирует обслуживание посетителя. Проверяет наличие свободных столов,"""
        for table in self.tables:
            self.table_status .append(table.is_busy)
        try:
            index = self.table_status.index(False)
            # print(f'Посетитель номер {self.customer} сел за стол {index + 1}', flush=True)
            self.tables[index].is_busy = True
            cust = Customer(index + 1, self.customer)
            cust.start()
            cust.join()
        except ValueError:
            print(f'Посетитель номер {self.customer} ожидает свободный стол')
            self.queue += 1

        # if False in self.table_status:
        #     print(f'Посетитель номер {self.person} сел за стол {table.number}', flush=True)

        # for table in self.tables:
        #     if not table.is_busy:
        #         print(f'Посетитель номер {self.person} сел за стол {table.number}', flush=True)
        #         table.is_busy = True
        #         break


class Customer(Thread):
    """класс (поток) посетителя. Запускается, если есть свободные столы."""
    def __init__(self, number, customer, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.number = number
        self.customer = customer

    def run(self):
        print(f'Посетитель номер {self.customer} сел за стол {self.number}', flush=True)
        sleep(5)
        print(f'Посетитель номер {self.customer} освободил стол {self.number}', flush=True)


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)


# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
