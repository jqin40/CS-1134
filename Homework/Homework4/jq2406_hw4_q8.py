def flat_list(nested_lst, low, high):
    #edge case
    if len(nested_lst) == 0:
        return []

    #base case: 1 "surface" element of nested_lst
    if low == high:
        if type(nested_lst[high]) == list:
            return flat_list(nested_lst[high], 0, len(nested_lst[high])-1)
        else:
            return [nested_lst[high]] #notice it's in a list! the recursive cases build onto this list
    #recursive case: >1 "surface" element of nested_lst
    #note: recursive case does high-1 to maintain the order of the list
    #      (base case is at low, and the rest get appended/extended after)
    else:
        prev = flat_list(nested_lst, low, high-1)
        if type(nested_lst[high]) == list:
            prev.extend(flat_list(nested_lst[high], 0, len(nested_lst[high])-1))
        else:
            prev.append(nested_lst[high])
        return prev

# def main():
#     # base case tests
#     lst = [[-2]]
#     print(flat_list(lst, 0, len(lst) - 1))
#     lst1 = [[[-2]]]
#     print(flat_list(lst1, 0, len(lst1) - 1))
#
#     # recursive case tests
#     lst2 = [[-2, [0]]]
#     print(flat_list(lst2, 0, len(lst2) - 1))
#     lst3 = [[1, 2], 3, [4, [5, 6, [7], 8]]]
#     print(flat_list(lst3, 0, len(lst3)-1))
#
#     # edge case tests
#     lst4 = []
#     print(flat_list(lst4, 0, len(lst4) - 1))
#     lst5 = [[]]
#     print(flat_list(lst5, 0, len(lst5) - 1))
#
# main()