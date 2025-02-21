from arraylist_module import ArrayList
class ArrayStack:
    def __init__(self):
        self.data = ArrayList()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self, val):
        self.data.append(val)
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data[-1]
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data.pop() #ArrayList pop, not ArrayStack pop


def eval_postfix_exp(exp_str):
    operators = "+-*/"
    exp_lst = exp_str.split()
    args_stk = ArrayStack()
    for token in exp_lst:
        if (token not in operators):
            args_stk.push(int(token))
        else:
            arg2 = args_stk.pop()
            arg1 = args_stk.pop()
            if token == '+':
                res = arg1 + arg2
            if token == '-':
                res = arg1 - arg2
            if token == '*':
                res = arg1 * arg2
            if token == '/':
                if arg2 == 0: raise ZeroDivisionError
                else:         res = arg1 / arg2
            args_stk.push(res)
    return args_stk.pop()

print(eval_postfix_exp("3 4 9 8 - * +"))