class Dog():
    def __init__(self, name, age, height, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.height = height

    def print_info(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Height", self.height)
        print("Color", self.color)
        print("Weight", self.weight)
        print("\n\n")

    def say_woof(self):
        print("Dog", self.name, "woofing. Woof-woof")

    def walk(self):
        print("Dog", self.name, "are walking around house")
