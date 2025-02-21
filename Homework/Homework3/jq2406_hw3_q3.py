def find_duplicates(lst):
# counts: keeps count of the number of each element seen.
# since the elements of the list must be from the domain [1, n-1],
# index 0 counts how many 1s there are
# index 1 counts how many 2s there are
# and so on, until index n-2 counts how many n-1s there are
    counts = [0] * (len(lst)-1)
    for elem in lst:
        counts[elem-1] += 1 #elem-1 is the index that counts elem
    result = []
    for i in range(len(counts)):
        if counts[i] > 1:
            result.append(i+1)
    return result

# def main():
#     lst = [2,4,4,1,2]
#     print(find_duplicates(lst))
#
# main()
