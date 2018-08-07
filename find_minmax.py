"""
Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).
Examples
[1, 2, 3, 4, 5] ➞ [1, 5]

[2334454, 5] ➞ [5, 2334454]

[1] ➞ [1, 1]
"""
def minMax(nums):
	return [min(nums), max(nums)]
