"""

Create a function that takes a list of non-negative numbers / strings and returns a new list without the strings.
Example
[1, 2, "a", "b"] ➞ [1, 2]

[1, "a", "b", 0, 15] ➞ [1, 0, 15]

[1, 2, "aasf", "1", "123", 123] ➞ [1, 2, 123]

"""

def filter_list(lst):
	aux_array = []
	for i in range(0, len(lst)):
		if not (isinstance(lst[i], str)):
			aux_array.append(lst[i])
			
	return aux_array
