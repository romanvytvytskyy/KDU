class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print("New hero!!!")
        print("Hero name is ", self.name)
        print("Health:", self.health)
        print("Armor:", self.armor)
        print("Power:", self.power)
        print("Weapon:", self.weapon)

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "felt in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "felt in battle")
                break


class Flash(Hero):
    def print_info(self):
        print()
