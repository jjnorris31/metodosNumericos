"""
Create a function that takes three arguments (x, y, z) and returns a list containing sublists (e.g. [[], [], []]), each of a certain number of items, all set to either a string or an integer.
x argument: Number of sublists contained within the main list.
y argument Number of items contained within each sublist(s).
z argument: Item contained within each sublist(s).
Examples
3, 2, 3 ➞ [[3, 3], [3, 3], [3, 3]]

2, 1, "edabit" ➞ [["edabit"], ["edabit"]]

3, 2, 0 ➞ [[0, 0], [0, 0], [0, 0]]

""

def matrix(x, y, z):
	result = []
	
	for i in range(0, x):
		result.append([z] * y)
		
	return result
