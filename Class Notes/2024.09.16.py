#Primality Test
def isPrime_v1(num):
    divs_count = 0
    for curr in range(1, num+1):
        if (num % curr == 0):
            divs_count += 1
    if (divs_count == 2):
        return True
    else:
        return False

#check up to half of the range
def isPrime_v2(num):
    divs_count = 0
    for curr in range(1, num//2+1):
        if (num % curr == 0):
            divs_count += 1
    if (divs_count == 1):
        return True
    else:
        return False

#check up to sqrt of the number
#At least one element is each pair of complementary divisors is <= sqrt(num).
def isPrime_v3(num):
    divs_count = 0
    for curr in range(1, num//2+1):
        if (num % curr == 0):
            divs_count += 1
    if (divs_count == 1):
        return True
    else:
        return False