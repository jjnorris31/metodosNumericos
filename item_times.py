"""
Create a function that takes two arguments (item, times). The first argument (item) is the item that needs repeating while the second argument (times) is the number of times the item is to be repeated. Return the result in a list.
Examples
"edabit", 3 ➞ ["edabit", "edabit", "edabit"]

13, 5 ➞ [13, 13, 13, 13, 13]

"7", 2 ➞ ["7", "7"]

0, 0 ➞ []
"""

def repeat(item, times):
	auxArray = []
	for x in range(0, times):
		auxArray.append(item)
	return auxArray
