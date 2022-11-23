from random import randint
from time import sleep


class Hero():
    def __init__(self, name, health, power, armor, weapon):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.weapon = weapon

    def print_info(self):
        print("New hero")
        sleep(1)
        print("Hero name is", self.name)
        sleep(1)
        print("Health:", self.health)
        sleep(1)
        print("Armor:", self.armor)
        sleep(1)
        print("Weapon:", self.weapon)
        sleep(1)

    def strike(self, enemy):
        print("Hit!", self.name, "attacking", enemy.name)
        sleep(1)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor:", enemy.armor, "and health:", enemy.health)
        sleep(1)

    def fight(self, enemy):
        while self.health > 0 or enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "felt in battle")
                sleep(1)
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "felt in battle")
                sleep(1)
                break


class Sponge(Hero):
    def __init__(self, name, health, power, armor, weapon):
        super().__init__(name, health, power, armor, weapon)

    def strike(self, enemy):
        print("Blow!!!", self.name, "attacking", enemy.name)
        sleep(1)
        enemy.armor = enemy.armor - randint(0, self.power)
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
            if randint(0, 100) > 50:
                self.health = self.health + randint(0, 5)
        print(enemy.name, "armor:", enemy.armor, "and health:", enemy.health)
        sleep(1)


class MyClass(Hero):
    # TODO Придумати і описати свій клас з одним унікальним методом
    pass
