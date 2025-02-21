def sum_to(n):
    """
    :n type: int
    :return type: int
    """
    if n==0: return n
    else: return n + sum_to(n-1) #else is optional

# print(sum_to(5)) #15

def product_evens(n):
    """
    :n type: int
    :return type: int
    """
    if n==2: return 2
    else: return n * product_evens(n-2) #else is optional
# print(product_evens(8)) #384

def find_max(lst, low, high):
    if low == high:
        return lst[low]
    prev = find_max(lst, low+1, high)
    if prev > lst[low]:
        return prev
    return lst[low]

# lst = [13,9,16,3,4,2]
# print(find_max(lst, 0, len(lst)-1))

#4
def is_palindrome(str, low, high):
    if low >= high:
        return True #base case: return True if 1 char or 0 chars left
    if str[low] != str[high]:
        return False
    return is_palindrome(str, low+1, high-1)

# print(is_palindrome("racecar", 0, 6)) #True
# print(is_palindrome("racecar", 1, 5)) #true
# print(is_palindrome("race car", 0, 6)) #false
# print(is_palindrome("racecar", 1, 3)) #false

#5
def vc_count(word, low, high):
    #base case: one character
    if low == high:
        if word[low].lower() in "aeiou":
            return (1,0)
        return (0,1)
    #recursive case: multi character
    v, c = vc_count(word, low+1, high)
    if word[low].lower() in "aeiou":
        return (v+1, c)
    return (v, c+1)

# word = "NYUTandonEngineering"
# print(vc_count(word, 0, len(word)-1)) #(8,12)

#6
def binary_search(lst, low, high, val):
    """
    :lst type: sorted list[int]
    :val type: int
    :low type, high type: int
    :return type: int (found), None
    """
    #base case: 1 value
    if low == high:
        if lst[low] == val:
            return low
        return None
    #recursive case: multivalue
    mid = (low+high)//2
    if lst[mid] == val:
        return mid
    elif lst[mid] > val:
        return binary_search(lst, low, mid-1, val)
    else: #lst[mid] < val
        return binary_search(lst, mid+1, high, val)

# nums = [4, 6, 7, 9, 11, 13, 15, 17, 19]
# target = 6
# target2 = 12
# print(binary_search(nums, 0, len(nums)-1, target))
# print(binary_search(nums, 0, len(nums)-1, target2))

#7
def list_sum_triangle(lst):
    """
    :lst type: list
    :output type: None
    """
    #base case: 1 element
    if len(lst) == 1:
        return print(lst)
        # return
    #recursive case: multiple elements
    nextlist = []
    for i in range(len(lst)-1):
        nextlist.append(lst[i]+lst[i+1])
    list_sum_triangle(nextlist)
    return print(lst)
    # return

lst = [1,2,3,4,5]
list_sum_triangle(lst)