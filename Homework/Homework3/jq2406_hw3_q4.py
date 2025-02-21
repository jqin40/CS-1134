#4b:
def remove_all(lst, value):
    #like move zeros, but shorten the list to remove the values
    #slow: keeps track of first target
    #fast: keeps track of the first non target AFTER SLOW
    fast = 0
    slow = 0
    while fast < len(lst): #fast goes here
        if lst[slow] != value:
            slow += 1
        else:
            #include slow > fast to make sure the swaps move the targets to the end of the list
            if lst[fast] == value or slow > fast:
                fast += 1
            else:
                lst[slow], lst[fast] = lst[fast], lst[slow]
                slow += 1
                fast += 1
    for i in range(len(lst)-slow):
        lst.pop()
    return lst


# def main():
    # lst = [2,4,4,1,2]
    # remove_all(lst, 2)
    # print(lst)

    # lst = [1,2,3,4,4,3,2,1]
    # remove_all(lst, 3)
    # print(lst)

# main()