def foo(n): #2^n
    #theta(n)
    # if n == 0: return 1
    # return 2 * foo(n-1)

    #theta(logn) -> divide n by 2
    # if n == 0: return 1
    # return 2**((n+1)//2) * foo(n//2)

    #alternative
    if n == 0 : return 1
    if n % 2 == 0:
        x = foo(n//2)
        return x * x
    #else, when n is odd
    x = foo(n//2)
    return x * x * 2

print(foo(6))