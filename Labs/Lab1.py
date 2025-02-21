# 2024-09-06

# lst=[1,2,3] #TODO: a random todo
# lst2=lst
# lst.append(4)
# lst2.append(5)
# print(lst)
# print(lst2)

# Coding Stuff
#1.
# def can_construct(word, letters):
#    lst = list(letters)
#    for i in range(len(word)):
#       letter = word[i]
#       if letter not in lst: return False
#       lst.remove(letter)
#    return True
#
# print(can_construct("apples", "aples"))
# print(can_construct("apples", "aplespl"))

# #2.
# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         a = self.a + other.a
#         b = self.b + other.b
#         return Complex(a, b)
#
#     def __sub__(self, other):
#         a = self.a - other.a
#         b = self.b - other.b
#         return Complex(a, b)
#
#     def __mul__(self, other):
#         a = self.a * other.a - self.b * other.b
#         b = self.a * other.b + self.b * other.a
#         return Complex(a, b)
#
#     def __repr__(self):
#         info = f"{self.a}+{self.b}i"
#         if self.b < 0:
#             info = info.replace('+', '')
#         return info
#
#     def __iadd__(self, other):
#         self.a += other.a
#         self.b += other.b
#         return self #need to do this or else it won't work
#
#
# cplx1 = Complex(5, 2)
# print(cplx1)  # 5 + 2i
#
# cplx2 = Complex(3, 3)
# print(cplx2)  # 3+3i
#
# print(cplx1 + cplx2)  # 8 + 5i
# print(cplx1 - cplx2)  # 2 - 1i
# print(cplx1 * cplx2)
# print(f"complex 1: {cplx1}")
# print(f"complex 2: {cplx2}")
#
# cplx1.__iadd__(cplx2)
# print(f"complex 1 after iadd: {cplx1}")

#3a.
import random
#TODO: fix this method
def create_permutation(n):
    lst = []
    for i in range(n):
        rand_index = random.randint(0, len(lst))
        lst.insert(rand_index, i)
    return lst

# list = create_permutation(6)
# print(list)

def scramble_word(word):
    word_list = list(word)
    perm = create_permutation(len(word))
    result = ''
    for i in range(len(word)):
        result += word_list[perm[i]]
    return result

# word = scramble_word("pokemon")
# print(word)

def play_game(word):
    scramble = scramble_word(word)
    print(f"Unscramble the word:   {' '.join(scramble)}")
    attempts = 0
    while attempts < 3:
        guess = input(f"Try #{attempts+1}: ")
        if guess != word:
            print("Wrong!")
            attempts += 1
        else:
            print("Yay, you got it!")
            break

# play_game("pokemon")
