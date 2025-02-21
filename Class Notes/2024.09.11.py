import sys
import copy

# lst1 = [1, [2, 3], 6]
# print(sys.getrefcount(6))
#
# lst2 = copy.deepcopy(lst1)
# x = 6
# print(sys.getrefcount(6))

## List Comprehension Reminder ##
# lst1 = [1, 2, 3, 6]
# lst2 = [x * x for x in lst1]
# print(lst2)

## Counter.py ##
# class Counter:
#     def __init__(self, name):
#         self.value = 0
#         self.name = name
#
#     def inc(self):
#           self.value += 1
#
#     def __repr__(self):
#         return str(self.value)
#
# c1 = Counter("BMW")
# print(c1)

## Revisiting simulating the range function ##
# for elem in range(3, 10, 0.5): #produces an error
#     print(elem)
def my_range2(start, stop, step):
    curr = start
    while(curr < stop):
        yield curr
        curr += step

for elem in my_range2(3, 10, 0.5):
    print(elem)
