"""
Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
Examples
[19, 5, 42, 2, 77] ➞ 7

[10, 343445353, 3453445, 3453545353453] ➞ 3453455

[2, 9, 6, -1] ➞ 8

[879, 953, 694, -847, 342, 221, -91, -723, 791, -587] ➞ 563

[3683, 2902, 3951, -475, 1617, -2385] ➞ 4519
"""

def sum_two_smallest_nums(lst):
	flag = 0
	sum = 0
	
	while flag < 2:
		if not (min(lst) < 0):
			sum += lst.pop(lst.index(min(lst)))
			flag += 1
		else: lst.pop(lst.index(min(lst)))
	
	return sum
