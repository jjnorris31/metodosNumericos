"""
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
Examples
[1, 2, 3, 4, 6, 7, 8, 9, 10] ➞ 5

[7, 2, 3, 6, 5, 9, 1, 4, 8] ➞ 10

[10, 5, 1, 2, 4, 6, 8, 3, 9] ➞ 7
"""

def missing_nums(lst):
	for i in range(1, 11):
		if i not in lst:
			return i
