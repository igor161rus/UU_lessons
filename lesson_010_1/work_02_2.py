import random
from collections import defaultdict
from multiprocessing import Process, Pipe

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Process):
    def __init__(self, name, worms, conn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.conn = conn

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is not None:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catched += 1
        print(f'{self.name}: Всего поймал {self.catched}', flush=True)
        self.conn.send([self.name, self.catched])
        self.conn.close()


global_fish_tank = defaultdict(int)

if __name__ == '__main__':

    humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава']
    fishers, pipes = [], []
    for name in humans:
        parent_conn, child_conn = Pipe()
        fisher = Fisher(name=name, worms=100, conn=child_conn)
        fishers.append(fisher)
        pipes.append(parent_conn)

    for fisher in fishers:
        fisher.start()
    total_fish = 0
    for conn in pipes:
        # name, fish_count = conn.recv()
        # или так:
        data = conn.recv()
        name, fish_count = data
        print('.' * 30, f'на берегу увидели: {name} поймал {fish_count}')
        total_fish += fish_count
    for fisher in fishers:
        fisher.join()

    print(f'Итого рыбаки поймали {total_fish} шт.')
