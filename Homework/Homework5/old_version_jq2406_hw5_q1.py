from ArrayStack import *
#TODO:are helper methods allowed? is is_numeric() allowed?
#TODO:#also are print statements allowed bc user input is needed?
def eval_postfix(exp_lst, variables):
    """
    :param exp_lst: list
    :param variables: dict of variables and their values
    :return: int or float of the expressions evaluated
    """
    args_stk = ArrayStack()
    for token in exp_lst:
        if token.isnumeric():
            args_stk.push(int(token))
        elif token in variables:
            args_stk.push(int(variables.get(token)))
        else:
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
            elif exp_lst[0].isnumeric():
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