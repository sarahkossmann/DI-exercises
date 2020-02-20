alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
string = input('write a sentence: ') #abc
shift = int(input('give me a number: ')) #3

def encrypt(text, shift): #in the func, need to call with param
    text.casefold()
    converted_string=list(text)
    final_string = ""

    for i in range(len(converted_string)): #by default, if write nothing it's 0
        for j in range(int(len(alphabet)/2)):
            if converted_string[i] == alphabet[j]:
                converted_string[i] = alphabet[j + shift]
                final_string = final_string + str(converted_string[i])
                break

    return final_string

print(encrypt(string, shift))                 

        
