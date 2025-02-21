# def linear_search(lst, val):
#     index = 0
#     count = 0
#     num = -1
#     while index < len(lst):
#         if lst[index] == val:
#             num = index
#             count += 1
#             if count == 2:
#                 return num
#         index += 1
#     return num
#
# def main():
#     print(linear_search([5,8,12,7,8,10], 8))

def linear_search(lst, val):
    for i in range(len(lst)): #depends on lst
        if (lst[i] == val):   #
            return i          #constant time
    return None