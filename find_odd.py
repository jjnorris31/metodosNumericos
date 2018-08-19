"""
Create a function that takes a list and finds the integer which appears an odd number of times.
Examples
[1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5] ➞ -1

[20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5] ➞ 5

[10] ➞ 10
"""

def find_odd(lst):
	for i in range(0, len(lst)):
		if lst.count(lst[i]) % 2 != 0:
			return lst[i]
	
