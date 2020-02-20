from Day4Week5Exercise import *
import random

jedi1 = Jedi("Jedi1")
jedi2 = Jedi("Jedi2")
jedi3 =Jedi("Jedi3")

sith1 = Sith("Sith1")
sith2 = Sith("Sith2")
sith3 = Sith("Sith3")

list_jedi = [jedi1, jedi2, jedi3]
list_sith = [sith1, sith2, sith3]

count = 0

while list_sith:
    count += 1
    jedi = random.choice(list_jedi)
    sith = random.choice(list_sith)


    if sith.fight(jedi):
        sith.train()
        jedi.train()
    else:
        list_sith.remove(sith)
        jedi.train()


    if count > 100:
        break

if count > 100:
    print("The Sith is taking over the Galaxy")
else:
    print("The Jedi won!")


