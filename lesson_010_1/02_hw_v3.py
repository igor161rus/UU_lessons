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


class WarehouseManager(Process):
    def __init__(self, request, data, *args, **kwargs):
        super(WarehouseManager, self).__init__(*args, **kwargs)
        self.request = request
        self.data = data

    def run(self):
        print(f'{self.request} parent process:', os.getppid())
        print(f'{self.request} process id:', os.getpid())
        self.process_request()

    def process_request(self):
        if self.request[0] not in self.data:
            self.data[self.request[0]] = self.request[2]
        elif 'receipt' in self.request:
            self.data[self.request[0]] += self.request[2]
        elif 'shipment' in self.request:
            self.data[self.request[0]] -= self.request[2]


if __name__ == '__main__':
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    data = Manager().dict()
    manager = WarehouseManager(requests, data)
    works = []
    for request in requests:
        req_work = WarehouseManager(request, data)
        works.append(req_work)
    for work in works:
        work.start()
    for work in works:
        work.join()
    print('*' * 20, '\n', manager.data)


# Результат
# C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe C:\pytnon\projects\UU_lessons\lesson_010_1\02_hw_v3.py
# ('product1', 'receipt', 100) parent process: 5416
# ('product1', 'receipt', 100) process id: 3184
# ('product2', 'receipt', 150) parent process: 5416
# ('product2', 'receipt', 150) process id: 6596
# ('product1', 'shipment', 30) parent process: 5416
# ('product1', 'shipment', 30) process id: 16968
# ('product3', 'receipt', 200) parent process: 5416
# ('product3', 'receipt', 200) process id: 19992
# ('product2', 'shipment', 50) parent process: 5416
# ('product2', 'shipment', 50) process id: 16636
# ********************
#  {'product1': 70, 'product2': 100, 'product3': 200}
#
# Process finished with exit code 0