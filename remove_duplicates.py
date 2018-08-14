"""
Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).
Examples
["John", "Taylor", "John"] ➞ ["John", "Taylor"]

[1, 0, 1, 0] ➞ [1, 0]

['The', 'big', 'cat'] ➞ ['The', 'big', 'cat']
"""

from collections import OrderedDict

def removeDups(lst):
	return list(OrderedDict.fromkeys(lst))
