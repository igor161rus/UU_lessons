from random import randint


class House:
    def __init__(self, need_loging):
        self.need_loging = need_loging
    def day_bar(self, day):
        pass

    def log(self):
        pass

class Child:
    def __init__(self, name, house, need_loging):
        self.name = name
        self.house = house
        self.need_loging =need_loging
    def act(self):
        pass

class Cat:
    def __init__(self, name, house, need_loging):
        self.name = name
        self.house = house
        self.need_loging =need_loging

class Wife(Man):
    color = 'magenta'
    FOOD_LEVEL_FOR_LIFE = 100
    DIRT_LEVEL_FOR_LIFE = 100
    HAPPINESS_LEVEL_FOR_LIFE = 40

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= self.FOOD_LEVEL_FOR_LIFE:
            self.house.money -= self.FOOD_LEVEL_FOR_LIFE
            self.house.food += self.FOOD_LEVEL_FOR_LIFE
            self.totals['spend_money'][1] += self.FOOD_LEVEL_FOR_LIFE
            self.totals['bought_food'][1] += self.FOOD_LEVEL_FOR_LIFE
            self.totals['shoping_days'][1] += 1
            self.log('{} купила еды'.format(self.name))
        else:
            self.log('{} нет денег на еду!'.format(self.name), color='red')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0
        self.totals['cleaned_dirt'][1] += 100
        self.totals['clean_days'][1] += 1
        self.log('{} убралась в доме'.format(self.name))

    def watch_series(self):
        self.fullness -= 10
        self.totals['watch_days'][1] += 1
        series_mood = randint(0, 1)
        if series_mood == 1:
            self.happiness += 5
            self.totals['happiness'][1] += 5
            self.log('{} смотрела сериал, осталась довольна'. format(self.name))
        else:
            self.happiness -= 5
            self.totals['happiness'][1] -= 5
            self.log('{} смотрела сериал, расстроилась'. format(self.name))

    def __init__(self, name, house, need_loging):
         self.name = name
         self.house = house
         self.need_loging = need_loging

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.totals['spend_money'][1] += 350
            self.totals['happiness'][1] += 60
            self.totals['bought_fur_cjat'][1] += 1
            self.log('{} купила шубу'.format(self.name))
        else:
            self.log('{} нет денег на шубу!'.format(self.name), color='red')
    def act(self):    #
        dice = randint(1, 6)
        if super().act():
            return
        elif self.house.food < self.FOOD_LEVEL_FOR_LIFE:
            self.shopping()
        elif self.happiness < self.HAPPINESS_LEVEL_FOR_LIFE:
            self.buy_fur_coat()
        elif self.house.dirt > self.DIRT_LEVEL_FOR_LIFE:
            self.clean_house()
        elif self.house.cat_food < self.CAT_EATING_POINTS_FOR_BUY:
            self.buy_cat_food()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.shopping()

        # if self.is_hungry:
        #     self.eat()
        # elif dice == 1:
        #     self.eat()
        # elif dice in [2, 3]:
        #     self.sleep()
        # else:
        #     self.soil()

def emulate_life(num_cats, need_loging=False):
    home = House(need_loging=True)
    vasya = Husband(name='', house=home, need_loging=need_loging)
    vasya.SALARY =250
    masha = Wife(name='', house=home, need_loging=need_loging)
    kolya = Child(name='', house=home, need_loging=need_loging)
    cat_names = ['', '', '',
                 '', '', '', '',
                 '', '', '', ]
    cats = [Cat(name=choice(cat_names), house=home, need_loging)
            for _ in range(num_cats)]

    somebody_is_dead = False
    for day in range(1, 366):
        home.day_bar(day)
        vasya.act()
        masha.act()
        kolya.act()
        if vasya.is_dead or masha.is_dead or kolya.is_dead:
            somebody_is_dead = True
        for cat in cats:
            cat.act()
            if cat.is_dead:
                somebody_is_dead = True
            if somebody_is_dead:
                home.log('', color='red')
                break
            vasya.log_man_info()
            masha.log_man_info()
            kolya.log_man_info()
            for cat in cats:
                cat.log_cat_info()
            home.log_house_info()

        if not somebody_is_dead:
            vasya.log_totals()
            masha.log_totals()
            kolya.log_totals()
            for cat in cats:
                cat.log_totals()

if __name__ == '__main__':
    emulate_life(num_cats=2, need_loging=True)