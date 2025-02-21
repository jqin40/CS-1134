#redid the count paths exceeding threshold in linkedbinarytree file
from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList

class BrowserHistory:
    def __init__(self):
        self.map = ChainingHashTableMap() #maps websites to (DLL node, # visits)
        self.dll = DoublyLinkedList() #DLL nodes contain website name only

    def __len__(self):
        return len(self.dll)

    def visit(self, website):
        if website not in self.map:
            node = self.dll.add_last(website)
            self.map[website] = (node, 1)
        else: #website in map
            node, visits = self.map[website]
            self.dll.delete_node(node)
            node = self.dll.add_last(website) #move the website node to the end by deleting previous one
            self.map[website] = (node, visits + 1)
        if len(self.dll) > 3:
            oldest_site = self.dll.delete_first()
            del self.map[oldest_site]

    def deleteHistory(self, website):
        if website not in self.map: return #don't do anything
        node = self.map[website][0]
        self.dll.delete_node(node)
        del self.map[website]

    def checkHistory(self):
        for site in self.dll:
            print(f"{site}: {self.map[site][1]} visits.")

# def main1():
#     myBrowser = BrowserHistory()
#     myBrowser.visit('gitHubbub.com')
#     myBrowser.visit('gitHubbub.com')
#     myBrowser.visit('hornHub.com')
#     myBrowser.visit('catPics.com')
#     myBrowser.visit('gitHubbub.com')
#     myBrowser.visit('CS1134isEASY.com')
#     print("Length:", len(myBrowser)) #3 because it only remembers the 3 most recently visited sites
#     myBrowser.checkHistory()
#     """
#     catPics.com: 1 visits.
#     gitHubbub.com: 3 visits.
#     CS1134isEASY.com: 1 visits.
#     """
#     myBrowser.deleteHistory("hornHub.com") #does nothing because it's not saved anymore
#     myBrowser.deleteHistory("catPics.com") #deletes catPics
#     print("")
#     myBrowser.checkHistory() #same as before but without catPics
#
# main1()

from ArrayStack import ArrayStack

class Company():
    def __init__(self):
        self.dll = DoublyLinkedList() #store order of all employees (employee_name, is_priority)
        self.stack = ArrayStack()

    def __len__(self):
        return len(self.dll)

    def addEmployee(self, employee_name, is_priority):
        node = self.dll.add_last((employee_name, is_priority))
        if is_priority:
            self.stack.push(node)

    def fire(self):
        if self.dll.is_empty():
            raise ValueError("Company is empty")
        name, priority = self.dll.delete_last()
        if priority:
            self.stack.pop()
        return name

    def fireFromPriorityDept(self):
        if self.stack.is_empty():
            return self.fire()
        name, priority = self.dll.delete_node(self.stack.pop())
        return name

    def displayEmployees(self):
        print([e for e in self.dll])

# def main2():
#     c = Company()
#     c.addEmployee("A", True)
#     c.addEmployee("B", False)
#     c.addEmployee("C", True)
#     c.addEmployee("D", True)
#     print(len(c))
#     c.displayEmployees()
#     print(c.fireFromPriorityDept()) #D
#     print(c.fire()) #C
#     print(c.fireFromPriorityDept()) #A
#     print(c.fireFromPriorityDept()) #B
#
# main2()

from LinkedBinaryTree import LinkedBinaryTree
# def level_list(root, level):
#     lst = []
#     #base
#     if level == 0:
#         if root:
#             lst.append(root.data)
#         return lst
#     #rec case
#     if root.left:
#         lst = level_list(root.left, level-1)
#     if root.right:
#         right = level_list(root.right, level-1)
#         lst.extend(right)
#     return lst

from ArrayQueue import ArrayQueue
def level_list(root,level):
    q=ArrayQueue()
    curlvl = 0
    result = [root]
    while curlvl < level:
        while len(result) != 0:
            q.enqueue(result.pop())
        while not q.is_empty():
            curr = q.dequeue()
            if curr.left:
                result.append(curr.left)
            if curr.right:
                result.append(curr.right)
        curlvl+=1
    for i in range(len(result)):
        result[i] = result[i].data
    return result

def main3():
    bt = LinkedBinaryTree()
    node1 = LinkedBinaryTree.Node(4)
    node2 = LinkedBinaryTree.Node(1)
    node3 = LinkedBinaryTree.Node(6, node1, node2)
    node4 = LinkedBinaryTree.Node(7)
    node5 = LinkedBinaryTree.Node(4, node4, node3)
    node6 = LinkedBinaryTree.Node(10)
    node7 = LinkedBinaryTree.Node(5, None, node6)
    node8 = LinkedBinaryTree.Node(2, node5, node7)
    node9 = LinkedBinaryTree.Node(8)
    node10 = LinkedBinaryTree.Node(19, node9)
    node11 = LinkedBinaryTree.Node(13)
    node12 = LinkedBinaryTree.Node(9, node10, node11)
    node13 = LinkedBinaryTree.Node(5, node12)
    node14 = LinkedBinaryTree.Node(1, node8, node13)
    bt.root = node14

    print(level_list(bt.root, 3)) #[7, 6, 10, 19, 13]
    print(level_list(bt.root, 6)) #[]

main3()

#singly linked list implementation
class PlayList:
    def __init__(self):
        self.map = ChainingHashTableMap() #(song_name, next_song_name)
        self.first = None
        self.last = None

    def add_song(self, new_song_name):
        if self.map.is_empty(): #alternative: if self.first is None, or self.last is None
            self.first = new_song_name
        else:
            self.map[self.last] = new_song_name
        self.map[new_song_name] = None
        self.last = new_song_name

    def add_song_after(self, song_name, new_song_name):
        if song_name not in self.map:
            raise KeyError("song_name not in play list")
        self.map[new_song_name] = self.map[song_name]
        self.map[song_name] = new_song_name

    def play_song(self, song_name):
        if song_name not in self.map:
            raise KeyError("song_name not in play list")
        print(song_name)

    def play_list(self):
        cursor = self.first
        while cursor is not None:
            self.play_song(cursor)
            cursor = self.map[cursor]

# def main4():
#     pl = PlayList()
#     pl.add_song("Feel It Still")
#     pl.add_song("Perfect")
#     pl.add_song("Havana")
#     pl.add_song_after("Perfect", "Thunder")
#     pl.add_song_after("Feel It Still", "Something Just Like This")
#     pl.play_song("Perfect") #Perfect
#     # pl.add_song_after("Havana", "Despacito")
#     pl.play_list() #Feel, Something, Perfect, Thunder, Havana
#
# main4()

def is_size_tree(bin_tree):
    result = is_size_tree_helper(bin_tree.root)
    return result

def is_size_tree_helper(root):
    #base
    if root is None: return (True, 0) #is_size, size
    #rec
    is_left, Lsize = is_size_tree_helper(root.left)
    is_right, Rsize = is_size_tree_helper(root.right)
    size = Lsize + Rsize + 1
    return (is_left and is_right and root.data == size, size)

#alternative solution with 1 return value
# def is_size_tree_helper(root):
#     #base
#     if root is None: return True
#     #rec
#     left = is_size_tree_helper(root.left)
#     right = is_size_tree_helper(root.right)
#     is_size = False
#     if root.left and root.right:
#         is_size = root.data == root.left.data + root.right.data + 1
#     elif root.left:
#         is_size = root.data == root.left.data + 1
#     elif root.right:
#         is_size = root.data == root.right.data + 1
#     else:
#         is_size = root.data == 1
#     return left and right and is_size

# def main5():
#     bt = LinkedBinaryTree()
#     node1 = LinkedBinaryTree.Node(1)
#     node2 = LinkedBinaryTree.Node(2, node1)
#     node3 = LinkedBinaryTree.Node(1)
#     node4 = LinkedBinaryTree.Node(1)
#     node5 = LinkedBinaryTree.Node(3, node3, node4)
#     # node6 = LinkedBinaryTree.Node(10)
#     node7 = LinkedBinaryTree.Node(1)
#     node8 = LinkedBinaryTree.Node(1)
#     node9 = LinkedBinaryTree.Node(3, node7, node8)
#     node10 = LinkedBinaryTree.Node(4, None, node9)
#     node11 = LinkedBinaryTree.Node(8, node5, node10)
#     node12 = LinkedBinaryTree.Node(11, node2, node11)
#     bt.root = node12
#     print(is_size_tree(bt))
# main5()