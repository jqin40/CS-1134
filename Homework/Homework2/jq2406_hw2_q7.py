def findChange(lst01):
    """
    :param lst01: list containing a sequence of 0s followed by a sequence of 1s
    :return: index of first 1
    """
    left = 0
    right = len(lst01)-1
    while left < right:
        mid = (left+right+1)//2 #try to get mid to land on the first 1
        if lst01[mid] == 0:
            left = mid
        else: #mid is on a 1
            if lst01[mid-1] == 0:
                return mid
            else: #element before mid is a 1
                right = mid

# def main():
#     lst01 = [0,0,0,0,0,1,1,1]
#     print(findChange(lst01)) #return 5
#
# main() #comment out when done