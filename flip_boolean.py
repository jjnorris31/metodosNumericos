"""
Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
Examples
True ➞ False

False ➞ True

0 ➞ "boolean expected"

None ➞ "boolean expected"
"""

def reverse(arg):

    if type(arg) == type(0) or arg == {}:
        result = "boolean expected"
    else:
        answersDict = {
            True: False,
            False: True
        }

        result = answersDict.get(arg, "boolean expected")

    return result
