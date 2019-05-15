class Man:
    food = 0

    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x += value
        Man.food += value


man = Man()
for i in range(10):
    man.x = i
    print(man.x, Man.food)
print(man.food)