# def sum_to(n):
#     for i in range(1, n+1):
#         total = i * (i+1)//2
#         yield total
#
# for i in sum_to(10):
#     print(i, end = ", ")

# #1a.
# def reverse_list(lst):
#     """
#     : lst type: list[]
#     : return type: None
#     """
#     for i in range((len(lst)+1) // 2):
#         lst[i], lst[-i-1] = lst[-i-1], lst[i]
#
# lst = [1,2,3,4,5,6]
# reverse_list(lst)
# print(lst)

# #1b
def reverse_list(lst, low=None, high=None):
    """
    : lst type: list[]
    : low, high type: int
    : return type: None
    """
    if (low==None):
        for i in range((len(lst)+1) // 2):
            lst[i], lst[-i-1] = lst[-i-1], lst[i]
    # """alternatively
    # if low == None:
    #     low = 0
    # if high == None:
    #     high = len(lst)-1
    # """
    else:
        for i in range((high-low+1) // 2):
            lst[i+low], lst[high-i] = lst[high-i], lst[i+low]

# lst = [1,2,3,4,5,6]
# reverse_list(lst)
# print(lst)
#
# lst2 = [1,2,3,4,5,6]
# reverse_list(lst2, 1, 3)
# print(lst2)

#2
# def powers_of_two(n):
#     for i in range(n):
#         yield 2**i
# print(list(powers_of_two(8)))

#3
def move_zeros(nums):
    """
    :nums type: list[int]
    :return type: None
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            #if nums[slow] == 0:
            #not necessary because the number at slow will always be nonzero
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
#     i=0
#     j=0
#     while i < len(nums):
#         if nums[i] == 0: i+=1
#         else:
#             if nums[j] != 0: j+=1
#             else:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i+=1
#                 j+=1

nums = [0, 1, 0, 3, 13, 0]
move_zeros(nums)
print(nums)

#4
def shift(lst, k):
    """
    : lst type: list
    : k type: int
    : return type: None
    """
    reverse_list(lst)
    reverse_list(lst, 0, k-1)
    reverse_list(lst, k, len(lst)-1)

# lst = [1,2,3,4,5,6]
# shift(lst, 2)
# print(lst)