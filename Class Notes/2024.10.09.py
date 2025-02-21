def recursive_sum(arr):
    if len(arr) == 0:                          #constant
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:]) #n-1

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, high)
    else:
        return binary_search(arr, target, low, mid-1)

