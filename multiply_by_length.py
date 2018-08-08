"""
Create a function to multiply all values in an array by the amount of items contained in that array.
Examples
[2, 3, 1, 0] ➞ [8, 12, 4, 0]
"""

def MultiplyByLength(arr):
	return list(map(lambda x: x * len(arr), arr))
