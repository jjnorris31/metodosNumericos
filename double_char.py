"""
Create a function that takes a string and returns a string in which each character is repeated once.
Examples
"String" ➞ "SSttrriinngg"

"Hello World!" ➞ "HHeelllloo  WWoorrlldd!!"

"1234!_ " ➞ "11223344!!__  "
"""

def double_char(txt):
	string_list = list(txt)
	result = []
	
	for i in range(0, len(string_list)):
		result.append(string_list[i])
		result.append(string_list[i])
	
	return ''.join(result)
