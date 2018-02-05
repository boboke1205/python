class Unit:
    isEnemy = False
    life = 100
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y, self.life)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


class Marin(Unit):
    def attack(self, unit):
        if self.isEnemy:
            unit.life = unit.life - 10


class Medic(Unit):
    def healing(self, unit):
        unit.life = unit.life + 10


enemy = Unit(36, 24)
print enemy.get()
enemy.setX(55)
print enemy.get()
enemy.setY(66)
print enemy.get()
enemy.move(24, 36)
print enemy.get()

marin = Marin(0, 0)
marin.attack(enemy)
print enemy.get()

