# Задание:
# Моделирование программы для управления данными о движении товаров на складе и эффективной обработки запросов на
# обновление информации в многопользовательской среде.
#
# Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на обновление информации о
# поступлении товаров и отгрузке товаров.
# Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти запросы в
# многопользовательской среде, с использованием механизма мультипроцессорности для обеспечения быстрой реакции на
# поступающие данные.
#
# Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
# Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
# Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
# Есть 2 действия: receipt - получение, shipment - отгрузка.
# а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа,
# если позиция уже была в словаре)
# б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
#
# 3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс, запускает его(start) и
# замораживает(join).
#
#
# Пример работы:
# # Создаем менеджера склада
# manager = WarehouseManager()
#
# # Множество запросов на изменение данных о складских запасах
# requests = [
#     ("product1", "receipt", 100),
#     ("product2", "receipt", 150),
#     ("product1", "shipment", 30),
#     ("product3", "receipt", 200),
#     ("product2", "shipment", 50)
# ]
#
# # Запускаем обработку запросов
# manager.run(requests)
#
# # Выводим обновленные данные о складских запасах
# print(manager.data)
#
# Вывод на консоль:
# {"product1": 70, "product2": 100, "product3": 200}
import os
from multiprocessing import Process


class WarehouseManager(Process):
    def __init__(self, *args, **kwargs):
        super(WarehouseManager, self).__init__(*args, **kwargs)
        self.data = dict()

    def run(self):
        # for i in requests:
        # print(i)
        # self.process_request(i)
        proc = WarehouseManager()
        proc.start()
        print(f'{self.data[i[0]]} parent process:', os.getppid())
        print(f'{self.data[i[0]]} process id:', os.getpid())
        proc.join()

    def process_request(self, requests):
        for i in requests:
            print(requests)
            if requests[0] not in self.data.keys():
                self.data[i[0]] = i[2]


if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    # manager.run(requests)
    manager.process_request(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)