"""
Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
Examples
8 ➞ [2, 4, 6, 8]

4 ➞ [2, 4]

2 ➞ [2]
"""

def find_even_nums(num):
	return [i for i in range(1, num + 1) if i % 2 == 0]
