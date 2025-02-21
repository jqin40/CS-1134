from DoublyLinkedList import *

class CompactString:
    def __init__(self, orig_str):
        ''' Initializes a CompactString object
        representing the string given in orig_str'''
        self.dll = DoublyLinkedList() #contains nodes with tuples

        if orig_str != '':
            start_char = ''
            count = 1
            for i in range(len(orig_str)):
                if i == 0:
                    start_char = orig_str[i]
                else:
                    if orig_str[i] == start_char:
                        count += 1
                    else: #different char
                        self.dll.add_last((start_char, count))
                        start_char = orig_str[i]
                        count = 1
            self.dll.add_last((start_char, count)) #add the last part

    def __len__(self):
        return len(self.dll)

    def __add__(self, other):
        ''' Creates and returns a CompactString object that
        represent the concatenation of self and other,
        also of type CompactString'''
        result = CompactString('')
        #edge case: empty strings
        if self.dll.header.next.data is None: #return copy of other
            curr_node = other.dll.header.next
            while curr_node.data is not None:
                result.dll.add_last(curr_node.data)
                curr_node = curr_node.next
            return result
        elif other.dll.header.next.data is None: #return copy of self
            curr_node = self.dll.header.next
            while curr_node.data is not None:
                result.dll.add_last(curr_node.data)
                curr_node = curr_node.next
            return result

        curr_node = self.dll.header.next
        while curr_node.data is not None:
            result.dll.add_last(curr_node.data)
            curr_node = curr_node.next

        #if last node of self and first node of other match, add the counts
        if result.dll.trailer.prev.data[0] == other.dll.header.next.data[0]:
            #note: can't modify tuple, replace with a new tuple
            new_count = result.dll.trailer.prev.data[1] + other.dll.header.next.data[1]
            result.dll.trailer.prev.data = (result.dll.trailer.prev.data[0], new_count)
        else: #just append the first node of other
            result.dll.add_last(other.dll.header.next.data)

        #copy the rest of the nodes in other
        curr_node = other.dll.header.next.next
        while curr_node.data is not None:
            result.dll.add_last(curr_node.data)
            curr_node = curr_node.next

        return result

    def __lt__(self, other):
        ''' returns True if self is lexicographically
        less than other, also of type CompactString'''
        def lt_helper(node_self, node_other):
            #remember to consider different length compactstrings later...
            #...and how an empty compact string would always come first?

            #base case: last node
            if node_self.next.data is None or node_other.next.data is None:
                #if letters are the same
                if node_self.data[0] == node_other.data[0]:
                    #return True this is the shorter dll, False otherwise
                    return node_self.data[1] < node_other.data[1]
                else: #letters not same, return the one that alphabetically earlier one
                    return node_self.data[0] < node_self.data[0]
            #recursive case: >1 node
            else:
                # if letters are the same
                if node_self.data[0] == node_other.data[0]:
                    # if counts are the same, recurse with next node
                    if node_self.data[1] == node_other.data[1]:
                        return lt_helper(node_self.next, node_other.next)
                    else:  # counts not same, return the lower count one NOT NEC CORRECT
                        #next few lines check if the shorter count one's next letter
                        #comes before the longer count one's current letter
                        if node_self.data[1] < node_other.data[1]:
                            return node_self.next.data[0] < node_other.data[0]
                        else: #node_other is shorter
                            return node_self.data[0] < node_other.next.data[0]
                else:  # letters not same
                    return node_self.data[0] < node_other.data[0]

        self_first = self.dll.header.next
        other_first = other.dll.header.next
        #edge cases: empty string (only has header and trailer)
        #empty string always comes alphabetically before nonempty string
        if self_first.data is None and other_first.data is None: return False
        elif self_first.data is None: return True
        elif other_first.data is None: return False
        return lt_helper(self_first, other_first)

    def __le__(self, other):
        ''' returns True if self is lexicographically
        less than or equal to other, also of type
        CompactString'''
        if self < other: return True
        #check if equal
        curr_self = self.dll.header.next
        curr_other = other.dll.header.next
        while curr_self.data is not None:
            if curr_self.data != curr_other.data: return False
            curr_self = curr_self.next
            curr_other = curr_other.next
        return True

    def __gt__(self, other):
        ''' returns True if self is lexicographically
        greater than other, also of type CompactString'''
        return other < self

    def __ge__(self, other):
        ''' returns True if self is lexicographically
        greater than or equal to other, also of type
        CompactString'''
        return other <= self

    def __repr__(self):
        ''' Creates and returns the original string representation
        (of type str) of self'''
        result = ''
        curr_node = self.dll.header.next
        while curr_node.data is not None:
            result += curr_node.data[0] * curr_node.data[1] #character * number
            curr_node = curr_node.next
        return result

# def main():
    # s1 = CompactString('aaaaabbbaaac')
    # print(s1.dll)
    # s2 = CompactString('aaaaaaacccaaaa')
    # print(s2.dll)
    # s3 = s2 + s1  # in s3’s linked list there will be 6 ’real’ nodes
    # print(s3.dll)
    # s4 = s1 + s2
    # print(s4.dll)
    # print(s1 < s2) #False because s1 goes alphabetically after s2
    # print(s1 > s2) #True
    # print(s2 < s1) #True
    # print(s2 > s1) #False
    # print(s1 < s4) #True because shorter
    # print(s4 < s1) #False because longer

    # string1 = CompactString('aab')
    # string2 = CompactString('aaab')
    # print('aab' <= 'aaab')
    # print(string1 <= string2)

    # s5 = CompactString('')
    # s6 = CompactString('')
    # s7 = s5 + s6
    # # print(s5.dll)
    # print(s5 < s1) #True
    # print(s5 < s5) #False
    # print(s1 < s5) #False
    # print(s1 > s5) #True
    # print(s5 <= s1) #True
    # print(s5 <= s5) #True
    # print(s1 <= s5) #False
    # print(s1 >= s5) #True
    # s6 = CompactString('ababa')
    # print(s6.dll)
    # print(s6 < s1) #False bc s1 goes alphabetically before
    # print(s6 > s1) #True
    # s7 = CompactString('ababa')
    # print(s6 < s7) #False
    # print(s6 <= s7) #True
    # print(s7 <= s7) #True
    # print(s6 >= s7) #True
    # print(s7 >= s7) #True
    # print(s7 >= s1) #True
    # print(s5 >= s1) #False
    # s8 = CompactString('')
    # print(s5 + s8) #empty string
    # print(s1 + s8) #s1
    # print(s8 + s2) #s2

# main()

# def main2():
#     s1 = CompactString('cccccc')
#     s2 = CompactString('c')
#     s3 = s1 + s2
#     print(s3.dll)
#
# main2()
#
# s1 = CompactString("")
# s2 = CompactString("")
# s3 = s1+s2
# print(s1 + s2)
# s1 = CompactString('aabbcdc')
# s2 = CompactString('aabbcbc')
# print(s1.dll)
# print(s2.dll)
# print(s1 > s2) #True