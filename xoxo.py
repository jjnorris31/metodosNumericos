"""
Create a function that takes a string, checks if it has the same number of 'x's and 'o's and returns either True or False.
Rules
Return a boolean value (True or False).
The string can contain any character.
When no x and no o are in the string, return True.
Examples
"ooxx" ➞ True

"xooxx" ➞ False

"ooxXm" ➞ True (case insensitive)

"zpzpzpp" ➞ True (returns true if no x and o)

"zzoo" ➞ False
"""

def XO(txt):
	if txt.count('x') + txt.count('o') == 0:
		return True
	else: return txt.count('x') + txt.count('X') == txt.count('o') 
