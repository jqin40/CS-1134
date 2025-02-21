#5a
def count_lowercase(s, low, high):
    #edge case
    if len(s) == 0:
        return 0
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    #base
    if low == high:
        if s[low] in lowercase:
            return 1
        else:
            return 0
    #recursive case
    else:
        if s[low] in lowercase:
            sum += 1
        return sum + count_lowercase(s, low+1, high)

# def main1():
#     s = "My name is Jason Qin"
#     print(count_lowercase(s, 0, len(s)-1)) #13
#     s1 = ""
#     print(count_lowercase(s1, 0, len(s1)-1))
#
# main1()

#5b
def is_number_of_lowercase_even(s, low, high):
    # edge case
    if len(s) == 0:
        return True #empty string = 0 lowercase
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    #base
    if low == high:
        if s[low] in lowercase:
            return False #1 lowercase
        else:
            return True #0 lowercase
        #alternatively, lines 28-31 can be condensed to line 33
        # return not s[low] in lowercase
    #recursive case
    else:
        if s[low] in lowercase:
            return not is_number_of_lowercase_even(s, low+1, high)
        else:
            return is_number_of_lowercase_even(s, low+1, high)

# def main2():
#     s = "My name is Jason Qin"
#     print(is_number_of_lowercase_even(s, 0, len(s)-1)) #False
#     s1 = ""
#     print(is_number_of_lowercase_even(s1, 0, len(s1)-1)) #True
#
# main2()