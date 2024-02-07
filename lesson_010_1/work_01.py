from collections import defaultdict
import random
import queue
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Thread):
    def __init__(self, name, worms, fish_tank, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.fish_tank = fish_tank

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}, {worm} - забросили, ждем...', flush=True)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}, {worm}: сожрали червяка...', flush=True)
            else:
                print(f'{self.name}, {worm}: поймал {fish} и хочет посадить его в садок', flush=True)
                if self.fish_tank.full():
                    print(f'{self.name}, {worm}: садок полон !!!', flush=True)
                self.fish_tank.put(fish)
                print(f'{self.name}, {worm}: наконец-то положил {fish} в садок', flush=True)
