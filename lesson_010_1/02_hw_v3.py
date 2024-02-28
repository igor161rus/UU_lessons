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
    def __init__(self, request, *args, **kwargs):
        super(WarehouseManager, self).__init__(*args, **kwargs)
        self.data = Manager().dict()
        self.works = []
        self.request = request
        # self.data_queue = Queue()

    def run(self):
        print(self.request)
        print(f'{self.request} parent process:', os.getppid())
        print(f'{self.request} process id:', os.getpid())
        # self.data_queue.put(self.data)

        # while not self.data_queue.empty():
        #     data = self.data_queue.get()
        #     print(data)

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


def main():
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager = WarehouseManager(requests)
    works = []
    for request in requests:
        req_work = WarehouseManager(request)
        works.append(req_work)
    for work in works:
        work.start()
    for work in works:
        work.join()
    print(manager.data)


if __name__ == '__main__':
    main()
