from itertools import permutations

class AnagramChecker:
    def __init__(self, word):
        self.words = open("words_list.txt", "r").read()
        all_words = self.words.split("\n")
        self.list_words = list(all_words)
        # print(self.list_words)


    def is_valid_word(self, word):
        for i in self.list_words:
            if word in self.list_words:
                print("Valid")
                break
            else:
                print("not a word")
                break

    def get_anagram(self, word):
        letter_list = list(word)
        perm_list = permutations(letter_list)
        temp = []
        for i in perm_list:
            # print(i)
            joined = (''.join(i))
            # print(joined)
            temp.append(joined)
        print(temp)
        anagrams_list = []
        for j in temp:
            if j in self.list_words:
                anagrams_list.append(j)
        print(anagrams_list)
        unique_list = set(anagrams_list)
        print(unique_list)

menu = input("")

word = AnagramChecker("something")
word.is_valid_word("EAT")
word.get_anagram("SLEEP")
