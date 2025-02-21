def two_sum(srt_lst, target):
    """
    Returns two indices (collected in a tuple) of two elements that add up to target,
    or None if no such indices are found.
    :param srt_lst: sorted list of integers
    :param target: integer
    :return: tuple of integers, or None
    """
    left = 0
    right = len(srt_lst)-1
    while left < right:
        if srt_lst[left] + srt_lst[right] == target:
            return (left, right)
        elif srt_lst[left] + srt_lst[right] < target:
            left += 1
        else:
            right -= 1
    return None

# def main():
#     srt_lst = [-2, 7, 11, 15, 20, 21]
#     target = 22
#     print(two_sum(srt_lst, target))
#
# main()