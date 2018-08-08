"""
Create a function that takes a list of numbers and returns a new list, sorted in ascending order (smallest to biggest).
Rules
Sort numbers list in ascending order.
If function's argument is an empty list, return an empty list.
Return a new list of sorted numbers.
Examples
[1, 2, 10, 50, 5] ➞ [1, 2, 5, 10, 50]

[80, 29, 4, -95, -24, 85] ➞ [-95, -24, 4, 29, 80, 85]

[] ➞ []
"""

def sortNumsAscending(lst):
	return sorted(lst)
