#todo: do #5

#1.
# def SortLst(lst):
#     index = 0
#     while index < len(lst):
#         if lst[index] != index:
#             temp = lst[index]
#             lst[index], lst[temp] = lst[temp], lst[index]
#         else: index+=1 #else is needed here to stay on the same index to keep making the swaps before moving on
#
# lst = [5,0,4,2,6,7,1,3]
# SortLst(lst)
# print(lst)

#2.
# def intersectionOfLst(lst1, lst2):
#     i = j = 0
#     overlap = []
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] == lst2[j]:
#             overlap.append(lst1[i])
#             i+=1
#             j+=1
#         elif lst1[i] < lst2[j]: i+=1
#         else: j+=1
#     return overlap
#
# lst1 = [1,2,3,4]
# lst2 = [3,4,5]
# print(intersectionOfLst(lst1, lst2))

#3.
# def isPowerOfTwo(n):
#     if n == 1: return True
#     elif n % 2 == 1: return False
#     return isPowerOfTwo(n/2)
#
# print(isPowerOfTwo(256))

#4.
# def split_parity(lst, low, high):
#     while low < high:
#         if lst[low] % 2 == 1 and lst[high] % 2 == 0:
#             lst[low], lst[high] = lst[high], lst[low]
#         if lst[low] % 2 == 0: low += 1
#         if lst[high] % 2 == 1: high -= 1
#
# lst = [4,-5,2,3,-1,-6,7,9,0]
# split_parity(lst, 0, len(lst)-1)
# print(lst)

