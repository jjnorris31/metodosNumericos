"""
Create a function that takes a list of numbers and returns a list where each number is the sum of itself + all previous numbers in the list.
Examples
[1, 2, 3] ➞ [1, 3, 6]

[1, -2, 3] ➞ [1, -1, 2]

[3, 3, -2, 408, 3, 3] ➞ [3, 6, 4, 412, 415, 418]
"""

def cumulative_sum(lst):
	for i in range(1, len(lst)):
		lst[i] = lst[i] + lst[i - 1]
	return lst
