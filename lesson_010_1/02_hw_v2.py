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
from multiprocessing import Process, Queue, Manager


class WarehouseManager:
    def __init__(self, requests):
        # super(WarehouseManager, self).__init__(*args, **kwargs)
        self.data = Manager().dict()
        self.works = []
        self.requests = requests
        # self.data_queue = Queue()

    def process_request(self, request):
        print(1 + 1)
        print(f'{request} parent process:', os.getppid())
        print(f'{request} process id:', os.getpid())
        # if request[0] not in self.data:
        # self.data[request[0]] = request[2]
        # elif 'receipt' in request:
        #     self.data[request[0]] += request[2]
        # elif 'shipment' in request:
        #     self.data[request[0]] -= request[2]

    def run(self):
        # self.data_queue.put(self.data)
        for request in self.requests:
            # req_work = Process(target=self.process_request(request))
            req_work = Process(target=self.process_request, args=[request])
            self.works.append(req_work)
        for work in self.works:
            work.start()
        # EOFError: Ran out of input
        for work in self.works:
            work.join()
        # while not self.data_queue.empty():
        #     data = self.data_queue.get()
        #     print(data)


def main():
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager = WarehouseManager(requests)
    manager.run()
    print(manager.data)


if __name__ == '__main__':
    main()
