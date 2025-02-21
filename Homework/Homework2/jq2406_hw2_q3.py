def factors(num):
    for i in range(1,int(num ** 0.5)+1):
        if num % i == 0:
            yield i
    for i in range(int(num ** 0.5), 0, -1):
        if num % i == 0 and i*i != num:
            yield num//i

# def main():
#     for curr_factor in factors(100):
#         print(curr_factor)
#
# main() #comment out when done