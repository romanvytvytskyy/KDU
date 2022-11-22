from time import sleep


class Hero():
    def __init__(self, name, health, armor, demage, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.demage = demage
        self.weapon = weapon

    def attack(self, enemy):
        print("Attack!! ", self.name, "attack", enemy.name)
        sleep(2)
        print("Hit!")
        sleep(2)
        enemy.armor = enemy.armor - self.demage
        if enemy.armor < 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor is", enemy.armor, "and", enemy.health)
        sleep(2)

    def print_info(self):
        print("New hero", self.name)
        sleep(2)
        print("Health", self.health)
        sleep(2)
        print("Armor", self.armor)
        sleep(2)
        print("Weapon", self.weapon)
        sleep(2)

    def fight(self, enemy):
        while self.health >= 0 or enemy.health >= 0:
            if enemy.health <= 0:
                print(enemy.name, "felt in battle")
                sleep(2)
                break
            if self.health <= 0:
                print(self.name, "felt in battle")
                sleep(2)
                break
            if enemy.health >= 0:
                self.attack(enemy)
            if self.health >= 0:
                enemy.attack(self)


class Grut(Hero):
    def __init__(self, name, health, armor, demage, weapon):
        super().__init__(name, health, armor, demage, weapon)

    def print_info(self):
        print("From deep space on the space ship coming new hero Grut")
        sleep(2)
        print("Grut health is", self.health, "and armor is ", self.armor)
        sleep(2)
        print("The hero haven't weapon and fight by himself")
        sleep(2)
