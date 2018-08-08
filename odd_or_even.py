"""
Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.
Examples
3 ➞ "odd"

146 ➞ "even"

19 ➞ 
"""

def isEvenOrOdd(num):
	if num % 2 == 0:
		return "even"
	else: return "odd"
