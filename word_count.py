"""
Create a function that takes a string and returns the word count. The string will be a sentence.
Examples
"Just an example here move along" ➞ 6

"This is a test" ➞ 4

"What an easy task, right" ➞ 5
"""

def count_words(txt):
	return len(txt.split())
