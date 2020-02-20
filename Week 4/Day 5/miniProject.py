tictactoe = [0,1,2,3,4,5,6,7,8]
print(tictactoe)

tictactoe2 = [
    [0,1,2],
    [3,4,5],
    [6,7,8]]
for row in tictactoe2:
    print(row)

def turn_x():
    ask_user = int(input('x, which box do you want to fill?: ')) 
    for i in tictactoe:
        if ask_user == i:
            tictactoe[i] = "x"
            print(tictactoe)
# turn_x()

def turn_o():
    ask_user = int(input('o, which box do you want to fill?: ')) 
    for i in tictactoe:
        if ask_user == i:
            tictactoe[i] = "o"
            print(tictactoe)
# turn_o()

def game():
    count = 1
    for i in tictactoe:
        count+=1
        if count%2 ==0:
            turn_x()
        else:
            turn_o()
game()




    