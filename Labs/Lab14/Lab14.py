from ChainingHashTableMap import *
#1.
# def most_frequent(lst):
#     #edge case
#     if lst == []: return None
#     map = UnsortedArrayMap() #maps the nums to their counts
#     num_with_max_count = -1 #temporary stub
#     for num in lst:
#         if num in map:
#             map[num] += 1
#             if map[num] > map[num_with_max_count]:
#                 num_with_max_count = num
#         else:
#             map[num] = 1
#             if len(map) == 1:
#                 num_with_max_count = num
#
#     return num_with_max_count

#still works with ChainingHashTableMap
#1a
def most_frequent(lst):
    #edge case
    if lst == []: return None
    map = ChainingHashTableMap(len(lst)) #maps the nums to their counts
    num_with_max_count = -1 #temporary stub
    for num in lst:
        if num in map:
            map[num] += 1
            if map[num] > map[num_with_max_count]:
                num_with_max_count = num
        else:
            map[num] = 1
            if len(map) == 1:
                num_with_max_count = num
    #alternatively, could use another loop to iterate through map to find highest count

    return num_with_max_count

# def main1a():
#     lst = [5,9,2,9,0,5,9,7]
#     print(most_frequent(lst))
# main1a()

#1b
def first_unique(lst):
    #edge case
    if lst == []: return None
    map = ChainingHashTableMap(len(lst)) #maps nums to their counts
    for num in lst:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    #now the map is filled nums as keys and counts as items
    for num in lst:
        if map[num] == 1:
            return num
    return None #no unique found

# def main1b():
#     lst = [5,9,2,9,0,5,9,7]
#     print(first_unique(lst))
# main1b()

#2.
def two_sum(lst,target):
    #note: edge case check not needed
    # if lst == []: return (None,None)
    #map stores the values as keys, indexes as items
    map = ChainingHashTableMap(len(lst)) #alternative name: seen
    for i in range(len(lst)):
        #note: lst[i] is key
        if (target-lst[i]) in map:
            return (map[target-lst[i]], i) #
        map[lst[i]] = i
    #loop finished, no pair exists
    return (None,None)

# def main2():
#     lst1 = [-2,11,15,21,20,7]
#     target1 = 22
#     print(two_sum(lst1, target1)) #(2,5)
#
#     lst2 = [-2,11,15,21,20,20]
#     target2 = 22
#     print(two_sum(lst2, target2)) #(None, None)
# main2()

from DoublyLinkedList import *
#TODO: Playlist
#3. implementation with dll and hashmap
class PlayList:
    def __init__(self):
        self.dll = DoublyLinkedList() #stores keys in the order of the playlist
        self.map = ChainingHashTableMap() #stores song names as keys, dll nodes as items
        # self.first = None
        # self.last = None

    def add_song(self,new_song_name):
        # if self.map.is_empty():
        #     self.map[new_song_name] = None
        #     self.first = new_song_name
        #     self.last = new_song_name
        # else:
        # new_song_node = DoublyLinkedList.Node(new_song_name)
        new_song_node = self.dll.add_last(new_song_name)
        self.map[new_song_name] = new_song_node

    def add_song_after(self, song_name, new_song_name):
        if song_name not in self.map: raise KeyError("song not in playlist")
        song_node = self.map[song_name]
        new_song_node = self.dll.add_after(song_node, new_song_name)
        self.map[new_song_name] = new_song_node

    def play_song(self, song_name):
        if song_name in self.map:
            print("Playing " + song_name)
        else:
            raise KeyError("song not in playlist")

    def play_list(self):
        for song_name in self.dll:
            print("Playing " + song_name)

def main3():
    p1 = PlayList()
    p1.add_song("Jana Gana Mana")
    p1.add_song("Kimi Ga Yo")
    p1.add_song("The Star-Spangled Banner")
    p1.add_song("March of the Volunteers")
    p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
    p1.add_song_after("Kimi Ga Yo", "Aegukga")
    p1.add_song("Arise, O Compatriots")
    p1.add_song("Chant de Ralliement")
    p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
    p1.add_song_after("Jana Gana Mana", "God Save The Queen")

    p1.play_song("The Star-Spangled Banner")
    p1.play_song("Jana Gana Mana")

    p1.play_list()
    # pl = Playlist()
    # pl.add_song("A")
    # pl.add_song("C")
    # pl.add_song("E")
    # pl.add_song("G")
    # pl.add_song_after("E","F")
    # pl.add_song_after("C","D")
    # pl.add_song("H")
    # pl.add_song("I")
    # pl.add_song_after("I","J")
    # pl.add_song_after("A","B")
    #
    # pl.play_song("C")
    # pl.play_song("A")
    # pl.play_list()

main3()
