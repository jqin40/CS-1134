#TODO: do optional 4?
from ArrayStack import *
#1.
def stack_sum(s):
    """
    :s type: ArrayStack
    :return type: int
    """
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        result = stack_sum(s)
        result += val
        s.push(val)
        return result

# def main1():
#     lst = [1,-14,5,6,-7,9,10,-5,-8]
#     s = ArrayStack()
#     for elem in lst:
#         s.push(elem)
#     print(stack_sum(s))
#
# main1()

#2.
def eval_prefix(exp_str):
    """
    :param exp_str: str
    :return type: int
    """
    exp_lst = exp_str.split()
    s = ArrayStack()
    for i in range(len(exp_lst)-1, -1, -1):
        if exp_lst[i].isdigit():
            s.push(exp_lst[i])
        elif exp_lst[i] in '+-*/':
            n1 = int(s.pop())
            n2 = int(s.pop())
            if exp_lst[i] == '+': s.push(n1+n2)
            elif exp_lst[i] == '-': s.push(n1-n2)
            elif exp_lst[i] == '*': s.push(n1*n2)
            else:
                if n2 == 0: raise ZeroDivisionError
                else: s.push(n1/n2)
    return s.top()

# def main2():
#     s1 = "- * 3 4 10"
#     print(eval_prefix(s1)) # 2
#     s2 = "+ * 5 5 / 10 2"
#     print(eval_prefix(s2)) # 30
#     s3 = "+ / - 10 2 4 8"
#     print(eval_prefix(s3)) # 10
#     s4 = "+ * 6 3 * 8 4"
#     print(eval_prefix(s4)) # 50
#     s5 = "+ - * 8 2 4 3 6"
#     print(eval_prefix(s5)) # 23
#
# main2()

#3
def flatten_list(lst):
    """
    :lst type: list
    :return type: None
    """
    s = ArrayStack()
    while len(lst) > 0:
        val = lst.pop()
        #to remove a list layer, pop the list and append all of the elements in the list
        if type(val) == list:
            for elem in val:
                lst.append(elem)
        else:
            s.push(val)
    while len(s) > 0:
        lst.append(s.pop())

# def main3():
#     lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
#     flatten_list(lst)
#     print(lst)
#
# main3()

#4
def stack_sort(s):
    """
    : input_str type:ArrayStack
    : return type:None
    """
    #use this to help with sorting
    helper_stack=ArrayStack()

def main4():
    lst = [1,-14,5,6,-7,9,10,-5,-8]
        s = ArrayStack()
        for elem in lst:
            s.push(elem)
    print(stack_sort(s))
main4()

