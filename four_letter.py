"""
Create a function that takes a list of strings. Return all words in the list that are exactly four letters.
Examples
["Ryan", "Kieran", "Jason", "Matt"] ➞ ["Ryan", "Matt"]

["Tomato", "Potato", "Pair"] ➞ ["Pair"]

["Kangaroo", "Bear", "Fox"] ➞ ["Bear"]
"""

def isFourLetters(lst):
	auxArray = [i for i in lst if len(i) == 4]
	return auxArray
