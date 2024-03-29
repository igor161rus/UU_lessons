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
from threading import Thread
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe(Thread):
    """класс для симуляции процессов в кафе"""

    def __init__(self, tables, *args, **kwargs):
        super(Cafe, self).__init__(*args, **kwargs)
        self.table = Queue()
        self.tables = tables
        self.customer = Queue()
        for i, table in enumerate(self.tables):
            self.table.put(i + 1)

    def customer_arrival(self):
        """моделирует приход посетителя(каждую секунду)."""
        for i in range(1, 21):
            customer = Customer(customer=i, table=0)
            self.customer.put(customer)
        while not self.customer.empty():
            customer = self.customer.get()
            print(f'Посетитель номер {customer.customer} прибыл', flush=True)
            self.serve_customer(customer=customer)
            sleep(1)

    def serve_customer(self, customer):
        """моделирует обслуживание посетителя. Проверяет наличие свободных столов,"""
        if not self.table.empty():
            table = self.table.get()
            customer.table = table
            customer.start()
        else:
            print(f'Посетитель номер {customer.customer} ожидает свободный стол')
            while self.table.empty():
                sleep(1)
            if not self.table.empty():
                table = self.table.get()
                customer.table = table
                customer.start()


class Customer(Thread):
    """класс (поток) посетителя. Запускается, если есть свободные столы."""

    def __init__(self, customer, table, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.table = table
        self.customer = customer

    def run(self):
        print(f'Посетитель номер {self.customer} сел за стол {self.table}', flush=True)
        sleep(5)
        print(f'Посетитель номер {self.customer} освободил стол {self.table}', flush=True)
        cafe.table.task_done()
        cafe.table.put(self.table)
        cafe.customer.task_done()
        cafe.customer.join()


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

# Результат:
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_010_1\01_hw_v3.py
# Посетитель номер 1 прибыл
# Посетитель номер 1 сел за стол 1
# Посетитель номер 2 прибыл
# Посетитель номер 2 сел за стол 2
# Посетитель номер 3 прибыл
# Посетитель номер 3 сел за стол 3
# Посетитель номер 4 прибыл
# Посетитель номер 4 ожидает свободный стол
# Посетитель номер 1 освободил стол 1
# Посетитель номер 4 сел за стол 1
# Посетитель номер 2 освободил стол 2
# Посетитель номер 5 прибыл
# Посетитель номер 5 сел за стол 2
# Посетитель номер 3 освободил стол 3
# Посетитель номер 6 прибыл
# Посетитель номер 6 сел за стол 3
# Посетитель номер 7 прибыл
# Посетитель номер 7 ожидает свободный стол
# Посетитель номер 4 освободил стол 1
# Посетитель номер 7 сел за стол 1
# Посетитель номер 5 освободил стол 2
# Посетитель номер 8 прибыл
# Посетитель номер 8 сел за стол 2
# Посетитель номер 6 освободил стол 3
# Посетитель номер 9 прибыл
# Посетитель номер 9 сел за стол 3
# Посетитель номер 10 прибыл
# Посетитель номер 10 ожидает свободный стол
# Посетитель номер 7 освободил стол 1
# Посетитель номер 10 сел за стол 1
# Посетитель номер 8 освободил стол 2
# Посетитель номер 11 прибыл
# Посетитель номер 11 сел за стол 2
# Посетитель номер 9 освободил стол 3
# Посетитель номер 12 прибыл
# Посетитель номер 12 сел за стол 3
# Посетитель номер 13 прибыл
# Посетитель номер 13 ожидает свободный стол
# Посетитель номер 10 освободил стол 1
# Посетитель номер 13 сел за стол 1
# Посетитель номер 11 освободил стол 2
# Посетитель номер 14 прибыл
# Посетитель номер 14 сел за стол 2
# Посетитель номер 12 освободил стол 3
# Посетитель номер 15 прибыл
# Посетитель номер 15 сел за стол 3
# Посетитель номер 16 прибыл
# Посетитель номер 16 ожидает свободный стол
# Посетитель номер 13 освободил стол 1
# Посетитель номер 16 сел за стол 1
# Посетитель номер 14 освободил стол 2
# Посетитель номер 17 прибыл
# Посетитель номер 17 сел за стол 2
# Посетитель номер 15 освободил стол 3
# Посетитель номер 18 прибыл
# Посетитель номер 18 сел за стол 3
# Посетитель номер 19 прибыл
# Посетитель номер 19 ожидает свободный стол
# Посетитель номер 16 освободил стол 1
# Посетитель номер 19 сел за стол 1
# Посетитель номер 17 освободил стол 2
# Посетитель номер 20 прибыл
# Посетитель номер 20 сел за стол 2
# Посетитель номер 18 освободил стол 3
# Посетитель номер 19 освободил стол 1
# Посетитель номер 20 освободил стол 2
#
# Process finished with exit code 0