#If you're reading this, this was a fun problem :)
def permutations(lst, low, high):
    #edge case test
    if len(lst) == 0:
        return [[]] #the empty list has only 1 permutation, which is itself
    #base
    if low == high:
        return [[lst[low]]] #2-layer list
    #recursive case
    else:
        #I use low+1 so that the first term is the original sequence,
        #although doing high-1 and using lst[high] also works
        prev = permutations(lst, low+1, high)
        result = []
        for i in range(len(prev)):
            for j in range(len(prev[i])+1): #plus one to account for inserting at the end
                perm = prev[i][:]
                perm.insert(j, lst[low])
                result.append(perm)
        return result

# def main():
#     lst = [1, 2, 3]
#     print(permutations(lst, 0, 2))
#     lst2 = [1,2,3,4]
#     print(permutations(lst2,0,3))
#
#     #edge case test
#     lst3 = []
#     print(permutations(lst3, 0, len(lst3)-1))
#
# main()

#old code from experimenting
# prev = [[1,2],[2,1]]
# result = []
# for i in range(len(prev)):
#     # print(f"before:{perm}")
#     for j in range(2):
#         perm = prev[i][:] #shallow copy is needed
#         perm.insert(0,3)
#         result.append(perm)
# print(result)