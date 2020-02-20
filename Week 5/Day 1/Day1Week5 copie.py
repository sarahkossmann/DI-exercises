# class Pet:
#     # name:
#     # species:
#     # color:
#     # age:
#     def __init__(self, specied, name, color): # allows you to initialize class
#         self.species = species
#         self.name = name
#         if color in ["pink", "blue"]:
#             print("stop colopainting you pet")
#         self.color = color

#     def eat(self):
#         print("eating mice")

#     def sleep(self):
#         print("18h a day")

#     def talk(self):
#         print(f'Meow! My name is {self.name}')
# # then you go to the terminal to call all the fucntions


# class House:
#     def __init__(self, city, num_rooms, landlord):
#         self.city = city
#         self.num_rooms = num_rooms
#         self.landlord = landlord
#         self.rent = 1000 * self.num_rooms
#         if city == "TA":
#             self.rent *= 2

#     def sign_contract(self, name, date):
#         if self.landlord == "Moti":
#             self.rent *= 2
#         print(f"Rental agreement between {name} and {self.landlord} for NI {self.rent}")
#     def complain_window(self):
#         print(f"{self.landlord} says Sorry")


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def talk(self):
        print("Wouaf")
    def jump(self):
        print(int(self.height * 2))
        