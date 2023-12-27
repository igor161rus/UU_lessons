class CanFly:

    def __init__(self):
        self.altitude = 0
        self.velocity = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return '{} {} {}'.format(
            self.__class__.__name__, self.altitude, self.velocity)


class Butterfly(CanFly):
    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.1


butterfly = Butterfly()
print(butterfly)
butterfly.take_off()
print(butterfly)
butterfly.fly()
print(butterfly)
butterfly.land_on()
print(butterfly)