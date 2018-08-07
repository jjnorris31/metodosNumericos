"""
Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.
Examples
[1, 2, 3] ➞ 3

['cat', 'dog', 'duck'] ➞ 'duck'

[True, False, True] ➞ True

[7, 'String', False] ➞ False
"""

def getLastItem(lst):
	return lst[-1]
