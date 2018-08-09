"""
Create a function that takes a list of numbers and returns the mean value.
Examples
[1, 0, 4, 5, 2, 4, 1, 2, 3, 3, 3] ➞ 2.54

[2, 3, 2, 3] ➞ 2.50

[3, 3, 3, 3, 3] ➞ 3.00
"""

def mean(lst):
	return round(sum(lst) / len(lst), 2)
