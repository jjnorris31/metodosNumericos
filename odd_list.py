"""
Create a function that takes a list of numbers and returns only the even values.
Examples
[1, 2, 3, 4, 5, 6, 7, 8] ➞ [2, 4, 6, 8]

[43, 65, 23, 89, 53, 9, 6] ➞ [6]

[718, 991, 449, 644, 380, 440] ➞ [718, 644, 380, 440]
"""

def noOdds(lst):
	return [i for i in lst if i % 2 == 0]
