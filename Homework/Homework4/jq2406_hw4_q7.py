def split_by_sign(lst, low, high):
    #base
    if low >= high: return lst
    #recursive case
    else:
        #pos, neg: swap and move both indices
        if lst[low] > 0 and lst[high] < 0:
            lst[low], lst[high] = lst[high], lst[low]
            return split_by_sign(lst,low+1,high-1)
        #pos, pos: move high
        elif lst[low] > 0 and lst[high] > 0:
            return split_by_sign(lst, low, high-1)
        #neg, pos: move both indices
        elif lst[low] < 0 and lst[high] > 0:
            return split_by_sign(lst, low+1, high-1)
        #neg, neg: move low
        else:
            return split_by_sign(lst, low+1, high)

# def main():
#     lst = [-2, -9, 4, 2,-1, 3, 8,-13]
#     print(split_by_sign(lst, 0, len(lst)-1))
#
#     lst1 = []
#     print(split_by_sign(lst1, 0, len(lst1)-1))
#
# main()