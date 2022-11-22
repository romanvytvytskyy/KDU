class Dog():
    def __init__(self, name, age, color, weight, height):
        self.name = name
        self.weight = weight
        self.age = age
        self.height = height
        self.color = color

    def say_woof(self):
        print("Dog", self.name, "woofing")

    def walk(self):
        print("Dog", self.name, "are walking around house")

    def print_info(self):
        print("Name: ", self.name)
        print("Age", self.age)
        print("Weight", self.weight)
        print("Color", self.color)
        print("Height", self.height)
        print("\n\n")
