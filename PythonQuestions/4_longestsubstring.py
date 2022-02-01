# Python3 program to find the length
# of the longest substring
# without repeating characters
def longestUniqueSubsttr(string):
	last_seen = {}
	start = 0
	longest = 0

	for i , c in enumerate(string):
		if c in last_seen and last_seen[c] >= start:
			print("character : "+c)
			start = last_seen[c] + 1
			print("start : "+str(start))
		else:
			longest = max(longest, i - start +1)
			print("longest : "+str(longest))

		print("start : "+str(start))
		last_seen[c] = i
		print("last_seen")
		print(last_seen)

	return longest



# Driver program to test the above function
string = "geeksforgeeks"
print("The input string is " + string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character" +
	" substring is " + str(length))
