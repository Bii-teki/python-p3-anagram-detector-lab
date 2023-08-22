class Anagram:
    def __init__(self, word):
        self.word_char = sorted([char for char in word])

    def match(self, word_list):
        matche = [word for word in word_list if sorted([char for char in word]) == self.word_char]

        return matche
          
         

    