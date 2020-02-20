# # l = [1,2,3,"a","b","c"]
# # l2 = []
# # l3 = []
# # for element in l:
# #     if type(element) == str:
# #         l2.append(element)
# #     else:
# #         l3.append(element)
# # print(l2)
# # print(l3)

# # my_list = ["o","oiqjdsoi","iza","ajljzqdjizjdsshfjh"]
# # for element in my_list:
# #     sortedlist = sorted(my_list, key=len)
# #     print((sortedlist[-1],))

# # # exercise 1

# # a = input('type a number: ')
# # b = input('typer another number')
# # if a > b:
# #     print('hello world')

# # # exercise 2

# x = int(input('type a number: '))
# y = int(input('type a second number: '))
# z = int(input('type a third number: '))
# numberList = [x,y,z]
# print(numberList)
# for element in numberList:
#     sortedNumber = sorted(numberList)
# print((sortedNumber[-1]))

# exercise 3

# askMonth = int(input('Insert a month from 1 to 12: '))
# if askMonth == 3 or askMonth == 4 or askMonth == 5:
#     print('spring')
# elif askMonth == 6 or askMonth == 7 or askMonth == 8:
#     print('summer')
# elif askMonth == 9 or askMonth == 10 or askMonth == 11:
#     print('autumn')
# else:
#     print('winter')

# exercise 4

# alphabet = input('Give me a letter')
# for element in alphabet:
#     if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u" or alphabet == "y" :
#         print('your letter is a vowel')
#     else:
#         print('your letter is a consonant')

# exercise 5
# import random
# random_num = random.randint(0,9)
# ask_num = int(input('type a number between 0 to 9: '))
# while True:
#     if random_num == ask_num:
#         print('number guessed!')
#         break
#     else:
#         ask_num = int(input('try again'))

# exercise 6

# my_list = []
# for number in range(1,21):
#     print(number)
#     my_list.append(number)

# exercise 8

# l = []
# for number in range(1,41):
#     print(number)
#     l.append(number)
# print(min(l))
# print(max(l))
# print(sum(l))

# exercise 9
# s = 6
# for element in range(1,s):
#     print(element * '*')

# exercise 10

# list_item = ["banana","orange","pineapple","orange"]
# idx = list_item.index("orange")
# print(idx)

# exercise 11
# list1 = [1,2,3]
# list2 = ["a","b","c"]
# list3 = list1.extend(list2)
# print(list1)

# exercise 12

# pizza_topping = input('Choose a topping: ')
# next_topping = ""
# while next_topping != 'quit':
#     next_topping = input('Choose another topping: ')
#     if next_topping == 'quit':
#         break
#     elif type(next_topping) == str:
#         pizza_topping = pizza_topping +' and '+ next_topping
#         print('I am adding ' + pizza_topping + ' on my pizza')

# exercise 13

# user_age = int(input('what is your age'))
# if user_age < 3:
#     print('your ticket is free')
# elif user_age > 3 and user_age < 12:
#     print('your ticket costs 10$') 
# elif user_age > 12:
#     print('your ticket costs 15$')

# exercise 14

# elements = [1,2,3,4,5] #5 becomes 4 after iteration and so becomes the last element => 4 and then becomes 3 etc (bc iteration is -1)
# i = len(elements)-1
# while i >= 0:
#     print(elements[i])
#     i= i-1

# exercise 15

store ={
"name": "Zara",
"creation_date": 1975, 
"creator_name": "Amancio Ortega Gaona", 
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color": 
{"France": "blue", 
"Spain": "red", 
"US": ["pink", "green"]
}
}
store["number_stores"] = 2
print(store)

 