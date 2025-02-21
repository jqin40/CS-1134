#Coding Section
# def is_palindrome(s):
#     """
#     : s type: str
#     : return type: bool
#     """
#     for i in range(len(s) // 2):
#         j = len(s)-1-i
#         if s[i] != s[j]: return False
#     return True
#
# print(is_palindrome("1racecar1"))
# print(is_palindrome("1racecar2"))
# print(is_palindrome("a"))

#2.
# # def is_vowel(s):
# #     return s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'
def reverse_vowels(input_str):
    vowels = 'aeiou'
    """
    :input-str type:string
    :return type: string
    """
    list_str = list(input_str)
    low, high = 0, len(input_str)-1
    while low < high:
        if list_str[low] in vowels:
            if list_str[high] in vowels:
                list_str[low], list_str[high] = list_str[high], list_str[low]
            high -= 1
        else: low += 1
    return "".join(list_str)
#
# print(reverse_vowels("tandon"))

#3. #TODO

#4. #TODO