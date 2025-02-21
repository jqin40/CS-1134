def e_approx(num):
    result = 0
    curr_factorial = 1
    for i in range(num+1):
        if i > 0: curr_factorial *= i
        result += 1 / curr_factorial
    return result

# def main():
#     for n in range(15):
#         curr_approx = e_approx(n)
#         approx_str = "{:.15f}".format(curr_approx)
#         print("n =", n, "Approximation:", approx_str)
#
# main() #comment out when done