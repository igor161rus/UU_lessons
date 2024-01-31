# Инструкции:
# Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.
#
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю,
# чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.
#
# Пример:
# knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
# knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
# knight1.start()
# knight2.start()
# knight1.join()
# knight2.join()
#
# Результат консоли (из-за гонки потоков может отличаться порядок вывода из потоков):
# Sir Lancelot, на нас напали!
# Sir Galahad, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, сражается 1 день(дня)...., осталось 80 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)...., осталось 60 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)...., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)...., осталось 20 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Galahad, сражается 5 день(дня)...., осталось 0 воинов.
# Sir Galahad одержал победу спустя 5 дней!
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней!
# Все битвы закончились!
#
# Примечание:
# В классе наследника (Knight), переопределите метод run, именно там будет заложена основная логика работы потоков.
# Используйте функцию sleep из модуля time для задержки времени.
import random
from threading import Thread, Lock
from time import sleep

lock = Lock()

class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        day = 1
        warriors = random.randrange(30, 100, 10)
        print(f'{self.name}: на нас напали {warriors} человек!', flush=True)
        for i in range(warriors, 0, -self.skill):
            remainder = warriors - self.skill
            with lock:
                print(f'{self.name}: сражается {day} день(дня)..., осталось '
                      f'{remainder if remainder > 0 else 0} воинов', flush=True)
            warriors -= self.skill
            day += 1
            sleep(5)
        with lock:
            print(f'{self.name}: одержал победу спустя {day - 1} дней!', flush=True)


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_010\02_hw.py
# Sir Lancelot: на нас напали 80 человек!
# Sir Lancelot: сражается 1 день(дня)..., осталось 70 воинов
# Sir Galahad: на нас напали 30 человек!
# Sir Galahad: сражается 1 день(дня)..., осталось 10 воинов
# Sir Lancelot: сражается 2 день(дня)..., осталось 60 воинов
# Sir Galahad: сражается 2 день(дня)..., осталось 0 воинов
# Sir Lancelot: сражается 3 день(дня)..., осталось 50 воинов
# Sir Galahad: одержал победу спустя 2 дней!
# Sir Lancelot: сражается 4 день(дня)..., осталось 40 воинов
# Sir Lancelot: сражается 5 день(дня)..., осталось 30 воинов
# Sir Lancelot: сражается 6 день(дня)..., осталось 20 воинов
# Sir Lancelot: сражается 7 день(дня)..., осталось 10 воинов
# Sir Lancelot: сражается 8 день(дня)..., осталось 0 воинов
# Sir Lancelot: одержал победу спустя 8 дней!
# Все битвы закончились!
#
# Process finished with exit code 0