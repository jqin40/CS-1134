def sum_squares(n):
    sum = 0
    for i in range(n):
        sum += i*i
    return sum

def sum_squares_lc(n):
    return sum([x*x for x in range(n)])

def sum_odd_squares(n):
    sum = 0
    for i in range(n):
        if i%2==1:
            sum+=i*i
    return sum

def sum_odd_squares_lc(n):
    return sum([x*x for x in range(n) if x%2==1])

def main():
    print(sum_squares(6)) #25+16+9+4+1 = 55
    print(sum_squares_lc(6))  # 25+16+9+4+1 = 55
    print(sum_odd_squares(6))  # 25+9+1 = 35
    print(sum_odd_squares_lc(6)) #25+9+1 = 35