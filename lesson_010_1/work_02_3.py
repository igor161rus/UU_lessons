import time
from collections import defaultdict
import random
from queue import Empty
from multiprocessing import Process, Pipe, Queue

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Process):
    def __init__(self, name, worms, catcher, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catcher = catcher

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}, {worm} - забросили, ждем...', flush=True)
            # time.sleep(random.randint(5, 20) / 10)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}, {worm}: сожрали червяка...', flush=True)
            else:
                print(f'{self.name}, {worm}: поймал {fish} и хочет посадить его в садок', flush=True)
                if self.catcher.full():
                    print(f'{self.name}, {worm}: помошник занят !!!', flush=True)
                self.catcher.put(fish)
                print(f'{self.name}, {worm}: наконец-то отдал {fish} помошнику', flush=True)


class Boat(Process):
    def __init__(self, worms_per_fisher, humans, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.catcher = Queue(maxsize=2)
        self.fish_tank = defaultdict(int)
        self.humans = humans

    def run(self):
        print('Лодка вышла в море...', flush=True)
        for name in self.humans:
            fisher = Fisher(name=name, worms=self.worms_per_fisher, catcher=self.catcher)
            self.fishers.append(fisher)
        for fisher in self.fishers:
            fisher.start()
        while True:
            try:
                fish = self.catcher.get(timeout=1)
                print(f'Приемщик принял {fish} и положил в садок', flush=True)
                self.fish_tank[fish] += 1
            except Empty:
                print(f'Приемщику нет рыбы в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой {self.fish_tank}', flush=True)


if __name__ == '__main__':
    boat = Boat(worms_per_fisher=10, humans=['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ])
    boat.start()
    boat.join()


