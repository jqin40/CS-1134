## 2 ##
# lst1 = [1, 2, 3]
# lst2 = lst1
# lst3 = [1, 2, 3]
# lst1.append(4)
# lst2.append(5)
# lst3.append(6)
# print("lst1 =", lst1)
# print("lst2 =", lst2)
# print("lst3 =", lst3)

## 2.5 ##
# s1 = "abc"
# s1.upper()
# print("s1 =", s1)
# s2 = s1.upper()
# print("s1 =", s1)
# print("s2 =", s2)

## 3 ##
# def main():
#     lst = [1, 2, 3]
#     s = "abc"
#     fun(lst, s)
#     print("main: lst =", lst, "s =", s)
#
# def fun(lst, s):
#     lst.append(6)
#     s = s.upper()
#     print("fun: lst =", lst, "s =", s)
#
# main()

# import sys
# x = "ABC"
# print(sys.getrefcount(x))

## 4 ##
# import copy
# lst1 = [1, 2, 3, 6]
# lst2 = copy.copy(lst1)
# lst2[0] = 10
#
# lst1 = [1, [2, 3], 4]
# lst2 = copy.copy(lst1)
# lst2[0] = 10
# lst2[1][0] = 20
#
# lst1 = [1, [2, 3], 4]
# lst2 = copy.deepcopy(lst1)
# lst2[0] = 10
# lst2[1][0] = 20
# print(lst1)
# print(lst2)

## Iterators ##
# s = "abc"
# for item in s:
#     print(item)
#
# #Simulating the for loop above
# s = "abc"
# s_iter = iter(s)
# end = False # flag to stop loop
# while(end == False):
#     try:
#         item = next(s_iter)
#         print(item)
#     except StopIteration:
#         end = True