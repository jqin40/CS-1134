def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid # target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 # Target not found

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    # arr = [1,2,3,4,5,6,7,8,9,10]
    # target = 8
    # result = binary_search(arr, target)
    # if result >= 0:
    #     print(f"{target} is found at index {result}")
    # else:
    #     print("Go away")
    arr = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(arr)
    print(sorted_array)

main()
