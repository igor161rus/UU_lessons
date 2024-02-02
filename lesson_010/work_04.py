import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Thread):
    def __init__(self, name, worms, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            # time.sleep(0.01)
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** 10000
            fish = random.choice(FISH)
            self.catch[fish] += 1


def time_track(func):
    def wrapper(*args, **kwargs):
        strted_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - strted_at, 6)
        print(f'{func.__doc__} работала {elapsed} секунд(ы)')
        return result

    return wrapper


@time_track
def run_in_one_threades(fishers):
    for fisher in fishers:
        fisher.run()


@time_track
def run_in_threads(fishers):
    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()


humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава']
fishers = [Fisher(name=name, worms=100) for name in humans]

run_in_one_threades(fishers)
run_in_threads(fishers)
