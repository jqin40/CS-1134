from ArrayStack import *

def is_int(num_string):
    """
    :param num_string: the number as a string
    :return: True if the num_string can be converted to int, False otherwise
    """
    if num_string[0] == "-":
        num_string = num_string[1:] #cut out the negative sign
    return num_string.isdigit()

def is_float(num_string):
    """
    :param num_string: the number as a string
    :return: True if the num_string can be converted to float, False otherwise
    """
    if num_string[0] == "-":
        num_string = num_string[1:] #cut out the negative sign
    if '.' in num_string:
        a,b = num_string.split('.')
        return a.isdigit() and b.isdigit()
    #not int, not float
    else:
        return False

def eval_postfix(exp_lst, variables):
    """
    :param exp_lst: list
    :param variables: dict of variables and their values
    :return: int or float of the expressions evaluated
    """
    args_stk = ArrayStack()
    for token in exp_lst:
        negator = 1
        if token[0] == '-' and len(token) > 1:
            negator = -1
            token = token[1:]

        if is_int(token):
            args_stk.push(int(token) * negator)
        elif is_float(token):
            args_stk.push(float(token) * negator)
        elif token in variables:
            args_stk.push(variables.get(token))
        elif token in '+-*/':
            arg2 = args_stk.pop()
            arg1 = args_stk.pop()
            if token == '+':
                res = arg1 + arg2
            elif token == '-':
                res = arg1 - arg2
            elif token == '*':
                res = arg1 * arg2
            else: # token == '/':
                if arg2 == 0: raise ZeroDivisionError
                else:         res = arg1 / arg2
            args_stk.push(res)
        else:
            raise Exception("Invalid token")
    return args_stk.pop()

def main():
    variables = {}
    while True:
        exp_str = input("--> ")
        exp_lst = exp_str.split()
        if len(exp_lst) == 1:
        #3 cases: done(), one number, or one variable
            if exp_lst[0] == "done()":
                break
            elif is_int(exp_lst[0]) or is_float(exp_lst[0]):
                print(eval_postfix(exp_lst, variables))
            else: #variable
                print(variables.get(exp_lst[0]))
        else: #len(exp_lst) > 1
        #3 cases: operations, assignment, or operations with assignment
            if '=' in exp_lst:
                #assign the number to the variable using a dictionary
                variables[exp_lst[0]] = eval_postfix(exp_lst[2:], variables)
                #print the name of the variable
                print(exp_lst[0])
            else: #just operations
                print(eval_postfix(exp_lst, variables))

main()