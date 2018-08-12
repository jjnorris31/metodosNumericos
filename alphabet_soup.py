"""
Create a function that takes a string and returns a string with its letters in alphabetical order.
Examples
"hello" ➞ "ehllo"

"edabit" ➞ "abdeit"

"hacker" ➞ "acehkr"

"geek" ➞ "eegk"

"javascript" ➞ "aacijprstv"
"""

def alphabet_soup(txt):
	return ''.join(sorted(txt))
