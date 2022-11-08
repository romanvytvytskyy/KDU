class Dog():
    def __init__(self, color, age, height, weight, name):
        self.color = color
        self.age = age
        self.height = height
        self.weight = weight
        self.name = name

    def say_woof(self):
        print("woof-woof")

    def print_info(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Color", self.color)
        print("Height", self.height)
        print('\n\n')

    def to_walk(self):
        print("Dog ", self.name, "is walking around house")
