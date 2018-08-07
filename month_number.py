"""
Write a function to return the name of the month as a string when provided an integer representing the month on the Gregorian calendar. Use the below table for reference. You can expect all test cases to provide a valid integer input.
#	Month Name
01	January
02	February
03	March
04	April
05	May
06	June
07	July
08	August
09	September
10	October
11	November
12	December
"""

def month_name(num):
	switcher = {
		1:	"January",
		2:	"February",
		3:	"March",
		4:	"April",
		5:	"May",
		6:	"June",
	  7:	"July",
		8:	"August",
		9:	"September",
		10:	"October",
		11:	"November",
		12:	"December"
	}
	
	return switcher.get(num, "Invalid month")
