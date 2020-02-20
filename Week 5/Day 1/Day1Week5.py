class Pet:
    # name:
    # species:
    # color:
    # age:
    def __init__(self, specied, name, color): # allows you to initialize class
        self.species = species
        self.name = name
        if color in ["pink", "blue"]:
            print("stop colopainting you pet")
        self.color = color

    def eat(self):
        print("eating mice")

    def sleep(self):
        print("18h a day")

    def talk(self):
        print(f'Meow! My name is {self.name}')
# then you go to the terminal to call all the fucntions


class House:
    def __init__(self, city, num_rooms, landlord):
        self.city = city
        self.num_rooms = num_rooms
        self.landlord = landlord
        self.rent = 1000 * self.num_rooms
        if city == "TA":
            self.rent *= 2

    def sign_contract(self, name, date):
        if self.landlord == "Moti":
            self.rent *= 2
        print(f"Rental agreement between {name} and {self.landlord} for NI {self.rent}")
    def complain_window(self):
#         print(f"{self.landlord} says Sorry")


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.winner = False

    def talk(self):
        print("Wouaf")
    def jump(self):
        print(int(self.height * 2))
    def fight(self, another_dog):
        if self.height > another_dog.height:
            return self
        else:
            return another_dog

Sarahs_dog = Dog("Teacup", 20)
Davids_dog = Dog("Rex", 50)

winner = Davids_dog.fight(Sarahs_dog)
print(f"the winner is {winner.name}")

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []


    def add_animals(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        print(self.animals)
    def sell_animals(self, bye_animals):
        self.animals.remove(bye_animals)
        print(f"Goodbye {bye_animals}")

    def sort_animals(self, animals):
        sorted_animals = self.animals.sort()
        print(sorted_animals)
        temp = 0
        pen = {}
        for x, y in zip(animals[::], animals[1::]):
            if x[0] == y[0]:
                pen[temp] = [x,y]
            else:
                temp += 1
                pen[temp] = x
                pen[temp] = y
        print(pen)



my_zoo = Zoo("Antwerp Zoo")
my_zoo.add_animals("Elephant")
my_zoo.add_animals("Zebra")
my_zoo.add_animals("Baboon")
my_zoo.add_animals("Bear")
my_zoo.add_animals("Kangaroo")
my_zoo.add_animals("Leopard")
my_zoo.add_animals("Lion")
my_zoo.get_animals()

# my_zoo.sell_animals("Zebra")
# my_zoo.get_animals()

my_zoo.sort_animals(my_zoo.animals)
my_zoo.get_animals()
        

class MenuManager:
    def __init__(self):
        self.menu = {}
    # def actual_menu(self):
    #     {  "Salad":{
    #             "name" : "Salad",
    #             "price": 40,
    #             "spice": "a",
    #             "gluten": True
    #         },
    #         "Pasta":{
    #             "name": "Penne Vodka",
    #             "price": 40,
    #             "spice": "a",
    #             "gluten": False
    #     }
    #     }
    def add_item(self, name, price, spice, gluten):
        menu_item = {
            "name": name,
            'price': price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu[name] = menu_item

    def print_menu(self):
        print(self.menu)

    def update_item(self, name, price, spice, gluten):
            if name in self.menu:
                self.menu[name]['price'] = price
                self.menu[name]['spice'] = spice
                self.menu[name]['gluten'] = gluten

            else:
                print(f"{name} is not on menu")

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            print(self.menu)
        else:
            print(f"{name} is not on menu")



    #     for count,item in enumerate(self.menu):
    #         print(count, item)
    #         if item['name'] == name:
    #             index_of_dict = count
    #     self.menu.pop(index_of_dict)
    #     # print(self.menu)
    #
    #     temp_list = []
    #     for item in self.menu:
    #         temp_list.append(item['name'])
    #     if name not in temp_list:
    #         print(f"{name} is not on menu")



# del p1.age
# del p1
new_dish = MenuManager()
new_dish.add_item("burger", 50, "c", True)
new_dish.print_menu()
new_dish.add_item("salad", 50, "c", True)
new_dish.print_menu()
new_dish.update_item("burger", 45, 'b', False)
new_dish.print_menu()

# print(new_dish.print_menu())
#
new_dish.remove_item("salad")
