import random
import statistics

class ForceWielder:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1,15)
        self.wisdom = random.randint(1,15)


    def train(self):
        pass


    def fight(self, other):
        # fight1 = self.power * self.wisdom/self.power + self.wisdom
        # fight2 = other.power * other.wisdom/ other.power + other.wisdom
        fight1 = statistics.harmonic_mean([self.power, self.wisdom])
        fight2 = statistics.harmonic_mean([other.power, other.wisdom])
        if fight1 > fight2:
            print(f"{self.name}, you are the winner!")
            return True
        else:
            print(f"{other.name}, you are the winner!")
            return False
        print(fight1)
        print(fight2)


    def is_jedi(self):
        pass

class Jedi(ForceWielder):
    def __init__(self, name):
        super().__init__(name)

        if self.wisdom > self.power:
            self.saber_color = 'green'
        elif self.power > self.wisdom:
            self.saber_color = 'blue'
        elif self.wisdom == self.power:
            self.saber_color = 'violet'

        self.wisdom = self.wisdom +10
        print(self.saber_color)
        print(self.wisdom)

    def train(self):
        self.wisdom = self.wisdom + random.randint(10, 20)
        self.power = self.power + random.randint(5, 15)

    def is_jedi(self):
        return True


class Sith(ForceWielder):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Darth " + name
        saber_color = "red"
        self.power = self.power +10
    def train(self):
        self.wisdom = self.wisdom + random.randint(5, 15)
        self.power = self.power + random.randint(10, 20)
    def is_jedi(self):
        return False



#
# p1 = ForceWielder("person1")
# p2 = ForceWielder("person2")
# p1.fight(p2)
#
# p3 = Jedi("Jason")
# print(p3.is_jedi())
#
# p4 = Sith("Antoine")
# print(f"{p4.name}")



