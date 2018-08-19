"""
Create a function that takes a single string as argument and returns an ordered list containing the indexes of all capital letters in the string.
Examples
"eDaBiT" ➞ [1, 3, 5]

"eQuINoX" ➞ [1, 3, 4, 6]

"determine" ➞ []

"STRIKE" ➞ [0, 1, 2, 3, 4, 5]

"sUn" ➞ [1]
"""

def indexOfCaps(word):
	return [word.index(i) for i in word if i.isupper()]
