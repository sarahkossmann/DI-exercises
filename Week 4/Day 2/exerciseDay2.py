# Exercise 2
# Create a set called my_fav_numbers with your favorites numbers.

# Add two new numbers to it.
num = {1,2,5,7}
new_num = num.union({2, 3, 4})
print(new_num)
# Remove the last one.
num.remove(7)
print(num)
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_num= {3,5,7,8}
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.
num.update(friend_num)
print(num)

# Exercise 3
# Do the same with a tuple.

t = (1,2,3,4,5)
l = list(t)
print(l)
l.extend([4,5,66])
print(l)
l.pop()
print(l)
friend_l = [2,4,8,9]
list3 = friend_l + l
print(list3)
t2 = tuple(l)
print(t2)

# Exercise 4
list = []
for number in range(0,9):
    print(number)
    list.append(number)
print(list)

list2 = []
x = range(1, 11)
for n in x:
  print(n)
  list2.append(n)
print(list2)

list3 = []
y = range(-9, 5)
for nu in y:
  print(nu)
  list3.append(nu)
print(list3)

list4 = []
y = range(10, 4, -1)
for num1 in y:
  print(num1)
  list4.append(num1)
print(list4)

list5 = []
y = range(1, 14, 2)
for num2 in y:
  print(num2)
  list5.append(num2)
print(list5)

list6 = []
y = range(1, 3)
for num3 in y:
  print(num3)
  list6.append(num3)

print(list6)



# ninja
import sys
import random
from copy import copy

user_string = input('Write something 10 characters long: ')
if len(user_string) != 10:
    print('Must be 10 characters long')
    sys.exit(1)
print(user_string)

info = f'first character: {user_string[0]}, last character: {user_string[-1]}'
print(info)

for i in range(1,len(user_string)+1):
    print(user_string[:i])

jumbled = copy(user_string)
random.shuffle(jumbled)
jumbled = ''.join(jumbled)

# extra exercise
menu_selection = None
menu_text = 'Welcome to the new menu\nPlease select what you would like to do:\na. print hello\nb.say your name\nx.exit'

while menu_selection !='x' :
    menu_selection = input(menu_text)
    if menu_selection == 'a':
        print('hello')
    elif menu_selection == 'b':
       user_name = input('Say your name')
       print(f'Hello {user_name}')
