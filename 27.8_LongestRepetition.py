# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(list):

	if len(list) < 1:
		return None

	longest = list[0]
	letter = list[0]
	maxCount = 1
	count = 1

	for i in range(1, len(list)):

		if list[i] == letter:
			count += 1

		else:
			if count > maxCount:
				maxCount = count
				longest = list[i-1]
			count = 1
			letter = list[i]

		if i == len(list)-1:
			if count > maxCount:
				maxCount = count
				longest = list[i-1]

	return longest
		

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([2,2,3,3,3])
# 1

print longest_repetition([])
# None

