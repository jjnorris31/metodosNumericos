"""
Instructions should be as straightforward as possible. The goal of a challenge is to test the user's ability to program; not to decipher confusing instructions.
Here are some example intros:
create a function that takes the two lowest numbers in a list, and return the sum of them
Examples
[5, 8, 12, 18, 22] ➞ 13

[4, 5, 8, 12,  86, 36] ➞ 9

[50, 2000, 10, 569, 64] ➞ 114
"""

def sum_lowest(numbers):
  return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))
