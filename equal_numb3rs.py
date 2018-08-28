"""
Write a function named equal that takes three input values (a, b, c) and returns the number of equal values.
Examples
equal(3, 4, 3) ➞ 2

equel(1, 1, 1) ➞ 3

equel(3, 4, 1) ➞ 0 
"""

def equal(a, b, c):
	if (a == b == c):
		return 3
	elif (a == b or a == c or c == b):
		return 2
	else: return 0
