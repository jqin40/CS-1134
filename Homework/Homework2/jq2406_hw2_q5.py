def split_parity(lst):
    left = 0
    right = len(lst)-1
    while left < right:
        # if left is even and right is odd, swap
        if lst[left] % 2 == 0 and lst[right] % 2 == 1:
            lst[left], lst[right] = lst[right], lst[left]

        # if left is odd, move on
        if lst[left] % 2 == 1:
            left+=1

        # if right is even, move on
        if lst[right] % 2 == 0:
            right-=1

# def main():
#     lst = [1, 2, 3, 4]
#     split_parity(lst)
#     print(lst)
#
# main() #comment out when done