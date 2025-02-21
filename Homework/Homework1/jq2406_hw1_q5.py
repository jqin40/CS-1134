def fibs(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        temp = a + b
        a = b
        b = temp

def main():
    for curr in fibs(8):
        print(curr)