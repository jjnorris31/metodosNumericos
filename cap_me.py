"""
Create a function that takes a list of names and returns a list with the first letter capitalized.
Examples
["mavis", "senaida", "letty"] ➞ ["Mavis", "Senaida", "Letty"]

["samuel", "MABELLE", "letitia", "meridith"] ➞ ["Samuel", "Mabelle", "Letitia", "Meridith"]

["Slyvia", "Kristal", "Sharilyn", "Calista"] ➞ ["Slyvia", "Kristal", "Sharilyn", "Calista"]
"""

def cap_me(lst):
	return [i.capitalize() for i in lst]
