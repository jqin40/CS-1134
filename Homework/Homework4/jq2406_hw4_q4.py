def list_min(lst, low, high):
    # edge case
    if len(lst) == 0:
        return None
    #base
    if low == high: return lst[low]
    #recursive case
    else:
        min_rest = list_min(lst, low+1, high)
        if lst[low] < min_rest:
            return lst[low]
        else: #min_rest < lst[low]
            return min_rest

# def main():
#     lst = [3,15,44,2,51,89,20]
#     print(list_min(lst, 0, len(lst)-1)) #2
#     lst1 = []
#     print(list_min(lst1, 0, 0)) #None
#
# main()