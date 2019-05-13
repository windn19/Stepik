class Human:
    def __init__(self, gender):
        self.sex = gender

    def __str__(self):
        return self.say+' you'

    def act(self):
        print(f'если я женщина - то смотрела: {self.sex("смотрел")}')


class Woman:
    def __init__(self, word):
        self.say = word

    def __str__(self):
        if self.say[-1] == 'л':
            self.say += 'а'
        else:
            self.say += 'ла'
        return self.say


class Man:
    food = 20

    def __init__(self, word):
        self.say = word
        self._x = 0

    def __str__(self):
        return self.say

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self.food = self.food + (value-self._x)
        self._x = value-self._x


man = Human(gender=Man)
woman = Human(gender=Woman)
woman_free = Woman('seed')
print(woman_free)
man.act()
woman.act()
woman1 = Human(gender=Woman)
man1 = Human(gender=Man)
woman1.act()
man1.act()
man2 = Man('seed')
food = 10
for i in [10, 1, 3, 4]:
    man2.x += i
    print(man2.x)
    print(man2.food)
    print()

