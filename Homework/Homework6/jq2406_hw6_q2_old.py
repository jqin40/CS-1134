from DoublyLinkedList import *

class Integer:
    def __init__(self, num_str):
        '''Initializes an Integer object representing
        the value given in the string num_str'''
        self.dll = DoublyLinkedList()
        for digit_char in num_str:
            self.dll.add_last(int(digit_char))

    def __add__(self, other):
        '''Creates and returns an Integer object that
        represent the sum of self and other, also of
        type Integer'''
        def add(node1, node2):
            #return tuple of ints to represent (digit, carry)
            sum = node1.data + node2.data
            digit = sum % 10
            carry = sum // 10
            return (digit, carry)

        node_self = self.dll.trailer.prev
        node_other = other.dll.trailer.prev
        result = Integer('0')
        node_result = result.dll.trailer.prev
        if len(self.dll) <= len(other.dll):
            for i in range(len(other.dll)):
                if i < len(self.dll):
                    digit, carry = add(node_self, node_other)
                    node_result.data += digit

                    if node_result.data >= 10:
                        carry += node_result.data // 10
                        node_result.data = node_result.data % 10
                    result.dll.add_first(carry)

                    #decrement
                    node_result = node_result.prev
                    node_self = node_self.prev
                    node_other = node_other.prev
                else: #all elements from self.dll have been added,
                    # now copy remaining digits from other, carrying if needed
                    node_result.data += node_other.data
                    if node_result.data >= 10:
                        node_result.data = node_result.data % 10
                        result.dll.add_first(1)
                    else:
                        #create a new node to left
                        result.dll.add_first(-1) #stub node to overwrite later

                    # decrement
                    node_result = node_result.prev
                    node_other = node_other.prev
        else: #len(self.dll) > len(other.dll)
            for i in range(len(self.dll)):
                if i < len(other.dll):
                    digit, carry = add(node_self, node_other)
                    node_result.data += digit
                    if node_result.data >= 10:
                        carry += node_result.data // 10
                        node_result.data = node_result.data % 10
                    result.dll.add_first(carry)

                    # decrement
                    node_result = node_result.prev
                    node_self = node_self.prev
                    node_other = node_other.prev
                else:  # all elements from other.dll have been added,
                    # now copy remaining digits from self, carrying if needed
                    node_result.data += node_self.data
                    if node_result.data >= 10:
                        node_result.data = node_result.data % 10
                        result.dll.add_first(1)
                    else:
                        # create a new node to left
                        result.dll.add_first(-1)  # stub node to overwrite later

                    # decrement
                    node_result = node_result.prev
                    node_self = node_self.prev
        #if there was no carry, remove the first node because it's a stub
        if result.dll.header.next.data == -1:
            result.dll.delete_first()
        return result

    def __repr__(self):
        ''' Creates and returns the string representation
        of self'''
        result = ''
        curr_node = self.dll.header.next
        for i in range(len(self.dll)):
            result += str(curr_node.data)
            curr_node = curr_node.next
        return result

def main():
    n1 = Integer('375')
    print(n1)
    n2 = Integer('4029')
    print(n2)
    n3 = n1 + n2
    print(n3) #4404
    n4 = n2 + n1
    print(n4) #4404

    n5 = Integer('1')
    print(n5)
    n6 = Integer('999')
    print(n6)
    n7 = n5 + n6
    print(n7) #1000
    n8 = n6 + n5
    print(n8) #1000

    n9 = n6 + n1
    print(n9) #1374
    n10 = n2 + n5 #TODO: debug this
    print(n10) #4030

main()