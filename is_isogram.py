"""
An isogram is a word that has no repeating letters, consecutive or nonconsecutive. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples
"Algorism" ➞ True

"PasSword" ➞ False (not case sensitive)

"Consecutive" ➞ False
"""

def is_isogram(txt):
	return len(list(set(txt.upper()))) == len(txt)
