def insertion_sort(lst):
    for curr_idx in range(1, len(lst)):
        curr = lst[curr_idx]
        j = curr_idx
        while j >= 1 and lst[j-1] > curr:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = curr
        