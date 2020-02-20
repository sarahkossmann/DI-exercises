import random

# YEAR = 2020
# MONTH = 2
# def get_age(year, month, day):
#     if month > MONTH:
#         age = YEAR - year -1
#     else:
#         age = YEAR - year
#     return age
# print(get_age(1990,3,1))

# def get_retired(sex, date_of_birth):
#     args = list(map(int,date_of_birth.split("/")))
#     day, month, year = args[0], args[1], args[2]
#     age = get_age(year, month, day)
#     print(f'your age {age}')
#     if sex == 'male':
#         return age >= 67
#     else:
#         return age >= 62
# print(get_retired("female", "1/5/1950"))

# def get_random_temp(season):
#     if season.lower() == "summer":
#         temp = random.randint(30, 40)
#     elif season.lower() == "fall":
#         temp = random.randint(20, 30)
#     elif season.lower() == "winter":
#         temp = random.randint(-10, 10)
#     elif season.lower() == "spring":
#         temp = random.randint(10, 20)
#     return temp
     
# def main():
#     month = int(input('what month is it?: '))
#     if month == 12 or month == 1 or month == 2:
#         season = "winter"
#     elif month >= 3 and month <= 5:
#         season = "spring"
#     elif month >= 6 and month <= 8:
#         season = "summer"
#     elif month >= 9 and month <= 11:
#         season = 'fall'
#     temp = get_random_temp(season)
#     print(f"The temperature is now {temp} degrees Celsius")
#     if temp < 0:
#         print('Brrrrr, that is freezing!')
#     elif temp > 0 and temp < 16:
#         print("Quite chilly! Do not forget your coat")
#     elif temp > 16 and temp < 23:
#         print("Do not forget your sunglasses")
#     elif temp > 23 and temp < 32:
#         print("Let's go to the beach")
#     elif temp > 32 and temp <40:
#         print("Way too hot!")
# main()

def throw_dice():
    toss = random.randint(1,6)
    return toss
def throw_until_double():
    dict ={}
    count = 1
    while True:
        die_1 = throw_dice()
        die_2 = throw_dice()
        dict [count] = (die_1, die_2)
        count += 1
        if die_1 == die_2:
            # print('you have reached double')
            # print(dict)
            # print(count-1)
            return count-1
def main():
    list = []
    i = 1
    while i<101:
        list.append(throw_until_double())
        i+=1
    print(list)
    # print(len(list))
    sum_of_list = sum(list)
    print(f"you threw dice {sum_of_list} times")
    average = sum_of_list/len(list)
    print(round(average,2))


    # for each in range(1,101):
    #     list.append(throw_until_double())
    # print(list)

main()