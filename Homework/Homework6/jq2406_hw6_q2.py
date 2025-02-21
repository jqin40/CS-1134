from DoublyLinkedList import *

class Integer:
    def __init__(self, num_str):
        '''Initializes an Integer object representing
        the value given in the string num_str'''
        self.dll = DoublyLinkedList()
        for digit_char in num_str:
            self.dll.add_last(int(digit_char))

    def __len__(self):
        #the number of digits in this Integer object
        return len(self.dll)

    def __add__(self, other):
        '''Creates and returns an Integer object that
        represent the sum of self and other, also of
        type Integer'''
        def pad_with_zeros(int_object, new_length):
            while len(int_object) < new_length:
                int_object.dll.add_first(0)

        # if the terms are different lengths,
        # pad the shorter one with zeros until it reaches desired length
        if len(self) < len(other):
            pad_with_zeros(self, len(other))
        elif len(self) > len(other):
            pad_with_zeros(other, len(self))

        node_self = self.dll.trailer.prev
        node_other = other.dll.trailer.prev
        result = Integer('0')
        node_result = result.dll.trailer.prev
        for i in range(len(self)):
            carry = 0
            sum = node_self.data + node_other.data
            node_result.data += sum

            if node_result.data >= 10:
                carry = 1
                node_result.data -= 10
            result.dll.add_before(node_result, carry)

            #decrement
            node_result = node_result.prev
            node_self = node_self.prev
            node_other = node_other.prev

        #if leading zero, remove
        if result.dll.header.next.data == 0:
            result.dll.delete_first()
        return result

    def __mul__(self, other):
        ''' Creates and returns an Integer object that
        represent the multiplication of self and other,
        also of type Integer'''
        def pad_with_zeros(int_object, new_length):
            while len(int_object) < new_length:
                int_object.dll.add_first(0)
        # def product_helper(node1, i, node2, j):
        #     return node1.data * 10**i + node2.data * 10**j
        def product_helper(node1, node2, node_product):
            carry = 0
            product = node1.data * node2.data
            node_product.data += product

            if node_product.data >= 10:
                carry = node_product.data // 10
                node_product.data %= 10
            product.dll.add_before(node_product, carry)
        def convert_product_dll(product_dll):
            #Resizes product_dll, for example:
            #Converts 400 to 4 <-> 0 <-> 0
            product_node = product_dll.trailer.prev
            while product_node.data is not None:
                if product_node.data >= 10:
                    carry = product_node.data // 10
                    digit = product_node.data % 10
                    product_node.data = digit
                    if product_node.prev.data is not None:
                        product_node.prev.data += carry
                    else: #prev is None
                        product_dll.add_before(product_node, carry)
                product_node = product_node.prev
            return product_dll


        # if the terms are different lengths,
        # pad the shorter one with zeros until it reaches desired length
        if len(self) < len(other):
            pad_with_zeros(self, len(other))
        elif len(self) > len(other):
            pad_with_zeros(other, len(self))

        node_self = self.dll.trailer.prev
        result = Integer('0')

        for i in range(len(self)):
            node_other = other.dll.trailer.prev
            for j in range(len(other)):
                carry = 0
                product = Integer('0')
                node_product = product.dll.trailer.prev
                node_product.data += node_self.data*10**i * node_other.data*10**j

                product.dll = convert_product_dll(product.dll)
                result += product

                # decrement
                node_other = node_other.prev
            node_self = node_self.prev
        return result


    def __repr__(self):
        ''' Creates and returns the string representation
        of self'''
        result = ''
        curr_node = self.dll.header.next
        is_leading_zero = True
        while curr_node.data is not None:
            #edge case: number is actually zero
            if len(self) == 1 and curr_node.data == 0:
                result += str(curr_node.data)
            if curr_node.data == 0 and is_leading_zero:
                pass
            else:
                is_leading_zero = False
                result += str(curr_node.data)
            curr_node = curr_node.next
        return result

# def main():
#     n1 = Integer('375')
#     print(n1)
#     n2 = Integer('4029')
#     print(n2)
#     n3 = n1 + n2
#     print(n3) #4404
#     print(n2) #375, no leading zero
#     n4 = n2 + n1
#     print(n4) #4404
#     n5 = Integer('1')
#     print(n5)
#     n6 = Integer('999')
#     print(n6)
#     n7 = n5 + n6
#     print(n7) #1000
#     n8 = n6 + n5
#     print(n8) #1000
#
#     n9 = n6 + n1
#     print(n9) #1374
#     n10 = n2 + n5
#     print(n10) #4030
#
#     # n11 = Integer('007')
#     # n12 = Integer('20')
#     # n13 = n11 + n12
#     # print(n13)
#
# main()

# def main2():
#     n1 = Integer('99')
#     n2 = Integer('99')
#     n3 = n1 * n2
#     # print(n3)
#
#     n4 = Integer('0')
#     n5 = n1 * n4
#     n6 = n4 * n1
#     print(n5)
#     print(n6)
#
#     n7 = Integer('1')
#     n8 = Integer('11')
#     n9 = n7 * n8
#     print(n9)
#
# main2()