"""
Create a function that takes a string and returns the number (count) of vowels contained within it.
Examples
"Celebration" ➞ 5

"Palm" ➞ 1

"Prediction" ➞ 4
"""

def count_vowels(txt):
	vowels = ['a', 'e', 'i', 'o', 'u']
	aux = 0
	for i in range(0, len(vowels)):
		aux += txt.count(vowels[i])
	return aux
