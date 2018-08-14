"""
Write a function that takes two strings and returns (True or False) whether they're anagrams or not.
Examples
'cristian', 'Cristina' ➞ True

'Dave Barry', 'Ray Adverb' ➞ True

'Nope', 'Note' ➞ False
"""

def is_anagram(s1, s2):
	return sorted(s1.lower()) == sorted(s2.lower())
	
