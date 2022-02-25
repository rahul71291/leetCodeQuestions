#solution1
def firstUniqChar1(s):
    """
    :type s: str
    :rtype: int
    """
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counts = [ 0 for rahul in range(26)]
    
    #iterate each character and store its count 
    #use ord() > It returns unicode of the character
    for c in s:
        print(ord(c))
        print(ord("a"))
        print(ord(c) - ord("a"))
        counts[ord(c) - ord("a")] += 1
        print (counts)
        x = list(set(s))
        x.sort()
        print(x)
        for i in x:
            print("Occurrence of  character {} in string {} is : {} ".format(i , s , counts[ord(i)-ord("a")]))
    for i,c in enumerate(s):
        if counts[ord(c) - ord("a")] == 1:
            return i
    return -1



#Solution 2
import collections
def firstUniqChar2(s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        print (count)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

print(firstUniqChar1("geeksforgeeks"))
print(firstUniqChar2("geeksforgeeks"))
            
        