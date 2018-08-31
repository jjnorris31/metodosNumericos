"""
You will be implementing a basic case of the map-reduce pattern in programming. Given a vector stored as a list of integers, find the magnitude of the vector. Use the standard distance formula for n-dimensional Cartesian coordinates.
Examples
[3, 4] ➞ 5

[0, 0, -10] ➞ 10

[] ➞ 0

[2, 3, 6, 1, 8] ➞ 10.677078252031311
"""

import math

def magnitude(lst):
	res = 0
	for x in lst:
		res += x**2
	return math.sqrt(res)
