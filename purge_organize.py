"""
Given a list of numbers, write a function that returns a list that...
Has all duplicate elements removed.
Is sorted from least to greatest value.
Examples
[1, 2, 4, 3] ➞ [1, 2, 3, 4]

[1, 4, 4, 4, 4, 4, 3, 2, 1, 2] ➞ [1, 2, 3, 4]

[6, 7, 3, 2, 1] ➞ [1, 2, 3, 6, 7]
"""

def unique_sort(lst):
	return sorted(list(set(lst)))
