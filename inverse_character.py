"""
Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.
Examples
Given that:

- "A" char code is: 65

- "a" char code is: 97

"A" ➞ 97

"a" ➞ 65
"""

def counterpartCharCode(char):
	return ord (char.swapcase())
