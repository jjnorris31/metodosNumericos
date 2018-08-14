"""
Count the amount of ones in the binary representation of an integer. So for example, since 12 is '1100' in binary, the return value should be 2.
Examples
0 ➞ 0

100 ➞ 3

999 ➞ 8
"""

def count_ones(num):
	return (bin(num)).count("1")
