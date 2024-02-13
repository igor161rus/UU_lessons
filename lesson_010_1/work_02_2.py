import random
from collections import defaultdict
from multiprocessing import Process

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Process):
    def __init__(self, name, worms, fish_tank, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is not None:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.fish_tank[fish] += 1
                self.catched += 1


global_fish_tank = defaultdict(int)

if __name__ == '__main__':

    humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава']
    fishers = [Fisher(name=name, worms=1000, fish_tank=global_fish_tank) for name in humans]

    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()

    total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
    total_fish_in_tank = sum(global_fish_tank.values())

    print(f'Итого рыбаки поймали {total_fish_from_fishers} шт., а с берега увидели {total_fish_in_tank} шт')
