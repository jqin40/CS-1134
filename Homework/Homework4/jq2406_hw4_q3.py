#3a
def print_triangle(n):
    #base
    if n == 1: print('*')
    #recursive case
    else:
        print_triangle(n-1)
        print('*' * n)

# def main1():
#     print_triangle(4)
#
# main1()

#3b
def print_opposite_triangles(n):
    #base
    if n == 1:
        print('*')
        print('*')
    #recursive case
    else:
        print('*' * n)
        print_opposite_triangles(n-1)
        print('*' * n)

# def main2():
#     print_opposite_triangles(4)
#
# main2()

#3c
def print_ruler(n):
    #base
    if n == 1: print('-')
    #recursive case
    else:
        print_ruler(n-1)
        print('-' * n)
        print_ruler(n-1)

# def main3():
#     print_ruler(4)
#
# main3()