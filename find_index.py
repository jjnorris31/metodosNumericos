"""
Create a function that takes a list and a string as arguments and return the index of the string.
Examples
['hi', 'edabit', 'fgh', 'abc'], 'fgh' ➞ 2

['Red', 'blue', 'Blue', 'Green'], 'blue' ➞ 1

['a', 'g', 'y', 'd'], 'd' ➞ 3

['Pineapple', 'Orange', 'Grape', 'Apple'], 'Pineapple' ➞ 0
"""

def find_index(lst, str):
	for i in range(0, len(lst)):
		if lst[i] == str:
			return i
	
