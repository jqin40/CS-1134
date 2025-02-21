#1a
# lst = [4,5,6]
# lst2 = lst
# lst.pop()
# lst2.append(7)
#
# print(lst)
# print(lst2)

#1b
# s = "DeF"
# s = s.upper()
# t = s
# t = t.lower()
# s = t.upper()
#
# print(s)
# print(t)

#1c
# s = "aBc"
# def func(s):
#     s = s.upper()
#     print("Inside func s =", s)
#     s = s.lower()
#
# func(s)
# print(s)

#1d
# lst = [4, 5, 6]
# def func(lst):
#     lst.pop()
#     lst = [7, 8, 9]
#     lst.append(7)
#     print("Inside func lst =", lst)
#
# func(lst)
# print(lst)

#2
# print([i//i for i in range(-3, 4) if i != 0])
# print(['Only Evens' [i] for i in range(10) if i % 2 != 0])
# print([((-i)**3) for i in range(-2, 5)])

#3a
# import copy
# lst = [1, 2, [3, 4]]
# lst_copy = copy.copy(lst)
# lst[0] = 10
# lst_copy[2][0] = 30
#
# print(lst)
# print(lst_copy)

#3b
# import copy
# lst=[1,[2,"abc"],[3,[4]],7]
# lst_deepcopy=copy.deepcopy(lst)
# lst[0]=10
# lst[1][1]="ABC"
# lst_deepcopy[2][1][0]=40
# print(lst)
# print(lst_deepcopy)

#3c
# lst=[1,[2,3],["a","b"]]
# lst_slice=lst[:]
# lst_assign=lst
# lst.append("c")
# for i in range(1,3):
#     lst_slice[i][0]*=2
# print(lst)
# print(lst_slice)
# print(lst_assign)

## Coding ##
#1.
# import copy
# class Polynomial:
#     def __init__(self, coefficients):
#         """
#         :type coefficients: list
#         """
#         if coefficients: self.coeff = coefficients
#         else: self.coeff = [0]
#     def __add__(self, other):
#         if len(self.coeff) > len(other.coeff):
#             result = copy.deepcopy(Polynomial(self.coeff))
#             for i in range(len(other.coeff)):
#                 result.coeff[i] += other.coeff[i]
#         else:
#             result = copy.deepcopy(Polynomial(other.coeff))
#             for i in range(len(self.coeff)):
#                 result.coeff[i] += self.coeff[i]
#         return result
#     def __call__(self, param):
#         sum = 0
#         for i in range(len(self.coeff)):
#             # print(self.coeff[i] * param ** i)
#             sum += self.coeff[i] * param ** i
#         return sum
#         # print(list(enumerate(self.coeff)))
#     #TODO: optional: repr, multiply, derive
#
# poly1=Polynomial([3,7,0,-9,2]) #represents 2x4-9x3+7x+3
# poly2=Polynomial([2,0,0,5,0,0,3]) #represents 3x6+5x3+2
# print(poly1.coeff)
# print(poly2.coeff)
# poly3=poly1+poly2
# print(poly3.coeff) #return[5,7,0,-4,2,0,3]
# print(poly1(1))#return3
# print(poly2(1))#return10
# print(poly3(1))#return13

#2.
# class UnsignedBinaryInteger:
#     def __init__(self, bin_num_str):
#         self.bin_num_str = bin_num_str
#     def decimal(self):
#         sum = 0
#         for i in range(len(self.bin_num_str)):
#             if self.bin_num_str[i] == '1':
#                 sum += 2**(len(self.bin_num_str) - i - 1)
#         return sum
#     def __lt__(self, other):
#         for i in range(len(self.bin_num_str):
#             if self.bin_num_str[i] != other.self.bin_num_str[i]:
#                 return self.bin_num_str[i] == 0
#
# thirteen = UnsignedBinaryInteger("1101")
# print(thirteen.decimal())

# print([(-2)**i for i in range(8)])
# print([int((i+1) * '1') for i in range(8)]) #int casting
