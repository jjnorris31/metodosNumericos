"""
Create a function that takes a list of positive and negative numbers. Return a list where the first element is the count of positive numbers and the second element is the sum of negative numbers.
Examples
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] ➞ [10, -65]

[92, 6, 73, -77, 81, -90, 99, 8, -85, 34] ➞ [7, -252]

[91, -4, 80, -73, -28] ➞ [2, -105]

[] ➞ []
"""

def sum_neg(lst):
	positive = 0
	negative = 0
	
	if not lst:
		return []
	
	for i in range(0, len(lst)):
		if lst[i] >= 0:
			positive += 1
		else:
			negative += lst[i]
	
	return [positive, negative]
