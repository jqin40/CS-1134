def appearances(s, low, high):
    #edge case
    if len(s) == 0:
        return {}
    #base
    if low == high:
        return {s[low]: 1}
    #recursive case
    else:
        prev = appearances(s, low+1, high) #get the dictionary from previous case before adding to it
        if s[low] not in prev:
            prev[s[low]] = 1
        else:
            prev[s[low]] += 1
        return prev

# def main():
#     phrase = "Hello world"
#     print(appearances(phrase, 0, len(phrase)-1))
#
# main()

