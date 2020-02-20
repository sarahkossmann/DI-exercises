class Animal:
    def __init__(self, legs, color, height, name):
        self.legs = legs
        self.color = color
        self.height = height
        self.name = name
        self.sleeping = False

    def sleep(self):
        self.sleeping = True
        return f"{self.name} is sleeping"
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def bark(self):
        return f"{self.name} barks"

class Shark(Animal):
    def sleep(self):
        return "sharks do not sleep"

dog = Dog(4, "red", "50 cm", "Sparky")
print(dog.sleep())
shark = Shark(0, "white", "50 cm", "Elvis")
print(shark.sleep())

a = Animal(4, "brown", "3 meters", "Titan")
print(a.sleeping)
a.sleep()