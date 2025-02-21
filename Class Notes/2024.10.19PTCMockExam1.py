#Question 6
# def find_max_under(k, n, low, high):
#     #base case
#     if low == high:
#         return n[low-1] #the element before the one that was searched
#     #recursive case
#     mid = (low+high)//2
#     if k > n[mid]:
#         return find_max_under(k, n, mid+1, high)
#     else: #k in smaller half
#         return find_max_under(k, n, low, mid)
#
# n = [1,2,3,5,8,13,21]
# k = 14
# print(find_max_under(k, n, 0, len(n)-1))

#Question 7
#iteratively
# def separate_num(lst):
#     left = 0
#     right = len(lst)-1
#     while left < right:
#         #if left even and right odd, swap
#         if lst[left] % 2 == 0 and lst[right] % 2 == 1:
#             lst[left], lst[right] = lst[right], lst[left]
#         #if left odd, increment
#         if lst[left] % 2 == 1: left += 1
#         #if right even, decrement
#         if lst[right] % 2 == 0: right -= 1
#
# lst = [3,15,44,2,51,89,20]
# separate_num(lst)
# print(lst)

#recursively
# def separate_num(lst, left, right):
#     #base
#     if left >= right: return lst
#     #recursive cases
#     #even odd
#     if lst[left] % 2 == 0 and lst[right] % 2 == 1:
#         lst[left], lst[right] = lst[right], lst[left]
#         return separate_num(lst, left+1, right-1)
#     #left odd
#     if lst[left] % 2 == 1: #left odd
#         return separate_num(lst, left+1, right)
#     #right even
#     if lst[right] % 2 == 0:
#         return separate_num(lst, left, right-1)
#     #the case of left odd, right even, takes more recursive calls but still gets done
#
# lst = [3,15,44,2,51,89,20]
# print(separate_num(lst, 0, len(lst)-1))

# for i in range(10,-1,-1):
#     print(i)

def move_zeroes(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
        if nums[slow] != 0:
            slow += 1

# nums = [0,1,0,3,13,0]
# move_zeros(nums)
# print(nums)

# #Consider these test cases!
# print("------ 3 ------")
# print("Zeroes in between list:")
# lst = [1, 0, 0, 13, 0, 3]
# print(f"{lst=}")
# move_zeroes(lst)
# print(f"{lst=} <- move_zeroes(lst)")
#
# print("Zeroes in front of list:")
# lst = [0, 0, 0, 1, 13, 3]
# print(f"{lst=}")
# move_zeroes(lst)
# print(f"{lst=} <- move_zeroes(lst)")
#
# print("Zeroes in back of list:")
# lst = [1, 13, 3, 0, 0, 0]
# print(f"{lst=}")
# move_zeroes(lst)
# print(f"{lst=} <- move_zeroes(lst)")

def remove_all_events(lst):
    left =0
    right = len(lst)-1
    #move evens to end
    while left < right:
        if lst[left] % 2 == 0 and lst[right] % 2 == 1:
            lst[left], lst[right] = lst[right], lst[left]
        if lst[left] % 2 == 1:
            left +=1
        if lst[right] % 2 == 0:
            right -=1
    #remove the evens
    popper = len(lst)-1
    while popper > right:
        lst.pop()
        popper -= 1

lst = [2, 3, 5, 2, 16, 13]
remove_all_events(lst)
print(lst)