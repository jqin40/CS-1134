def shift(lst, k, dir='left'):
    if dir == 'left':
        while k > 0:
            for i in range(len(lst)-1):
                lst[i], lst[i+1] = lst[i+1], lst[i]
            k -= 1
    elif dir == 'right':
        while k > 0:
            for i in range(len(lst)-1):
                #the right index is len-i-1, left is len-i-2
                lst[len(lst)-i-1], lst[len(lst)-i-2] = lst[len(lst)-i-2], lst[len(lst)-i-1]
            k -= 1

def main():
    lst = [1,2,3,4,5,6]
    shift(lst,2,"right")
    print(lst)