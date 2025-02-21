from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    """
    Takes a list of integers
    Returns a list containing all the different
    permutations of the elements in lst
    """
    #edge case: empty list
    if len(lst) == 0:
        return []

    s = ArrayStack()
    q = ArrayQueue()
    #copy list into stack
    for i in range(len(lst)-1,-1,-1):
        s.push(lst[i])

    for j in range(len(s)):
        if j == 0:
            q.enqueue([s.pop()])
        else:
            curr_perm = q.first() #ex: consider perms for (1,2,3), curr_perm is [1,2]
            while len(curr_perm) == j:
                for i in range(len(curr_perm),-1,-1):
                    orig_perm = curr_perm[:] #shallow copy to revert back to it after each iteration
                    curr_perm.insert(i,s.top())
                    q.enqueue(curr_perm)
                    curr_perm = orig_perm
                q.dequeue() #dequeue because perms with [1,2] are done
                curr_perm = q.first() #now check the next perm [2,1]
            s.pop()

    result = []
    while not q.is_empty():
        result.append(q.dequeue())

    return result

# def main():
#     lst = [1,2]
#     print(permutations(lst))
#     lst2 = [1,2,3]
#     print(permutations(lst2))
#     lst3 = [1]
#     print(permutations(lst3))
#     lst4 = []
#     print(permutations(lst4))
#     lst5 = [1,2,3,4]
#     print(permutations(lst5))
#     lst6 = [1,1]
#     print(permutations(lst6))
#
# main()
