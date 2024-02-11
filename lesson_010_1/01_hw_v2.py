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
import random
from datetime import time
from threading import Thread
from time import sleep
import queue


class Table:
    def __init__(self, number, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)
        self.number = number
        self.is_busy = False


class Cafe(Thread):
    """класс для симуляции процессов в кафе"""

    def __init__(self, tables, *args, **kwargs):
        super(Cafe, self).__init__(*args, **kwargs)
        self.queue = queue.Queue()
        self.tables = tables
        self.table_status = []
        self.customer = queue.Queue()

    # def run(self):
    #     for table in self.tables:
    #         self.queue.put(table)

    def customer_arrival(self):
        """моделирует приход посетителя(каждую секунду)."""
        for table in self.tables:
            self.queue.put(table)
        for i in range(1, 6):
            self.customer.put(i)
        numb_customer = self.customer.get()
        print(f'Посетитель номер {numb_customer} прибыл', flush=True)
        # sleep(1)
        # for i in range(1, 6):
        #     sleep(1)
        #     self.customer.put(i)
        # cust = Customer(customer=numb_customer, table=0)
        # self.queue.put(customer)
        # self.serve_customer(cust)
        self.serve_customer(numb_customer)

    def serve_customer(self, customer):
        """моделирует обслуживание посетителя. Проверяет наличие свободных столов,"""
        for table in self.tables:
            self.table_status.append(table.is_busy)
        # while not self.customer.empty():
        while not self.queue.empty():
            try:

                # index = self.table_status.index(False) + 1
                # self.tables[index].is_busy = True
                # self.customer.get()
                # i = Customer(j, index)
                print(f'Обслуживается посетитель номер {self.customer}', flush=True)
                # sleep(5)
                cust = Customer(customer=self.customer.get(), table=self.queue.get())
            except ValueError:
                print(f'Посетитель номер {self.customer} ожидает свободный стол')


class Customer(Thread):
    """класс (поток) посетителя. Запускается, если есть свободные столы."""

    def __init__(self, customer, table, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.table = table
        self.customer = customer

    def run(self):
        # cust = Customer(customer=cafe.customer, table=0)
        # cust.table = index
        cafe.cust.start()
        cust.join()
        print(f'Посетитель номер {self.customer} сел за стол {self.table}', flush=True)
        sleep(5)
        print(f'Посетитель номер {self.customer} освободил стол {self.table}', flush=True)
        tables[self.table].is_busy = False


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
