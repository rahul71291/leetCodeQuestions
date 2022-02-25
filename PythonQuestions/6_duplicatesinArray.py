import collections
def findDuplicates(arr):
    duplicates = 0
    count = collections.Counter(arr)

    print(count)

    for c in count:
        if (count[c] > 1 ):
            print ("The number {} in the given array is occuring {} times " . format(c,count[c]))
            duplicates = 1
        else:
            print ("The number {} in the given array is occuring {} times " . format(c,count[c]))
            
    if not duplicates:
        print("No duplicates in the array")
#arr = [1,2,3,1,4,6,2,4,0,3,4,5]
arr = [1,2,3,4,5,6,7,8,9]
findDuplicates(arr)

