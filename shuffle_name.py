"""
Create a function that takes a string (will be a persons first and last name) and returns a string with the first and last name swapped.
Examples
"Donald Trump" ➞ "Trump Donald"

"Rosie O'Donnell" ➞ "O'Donnell Rosie"

"Seymour Butts" ➞ "Butts Seymour"
"""

def name_shuffle(txt):
	list = txt.split()
	list[0], list[1] = list[1], list[0]
	return " ".join(list)
