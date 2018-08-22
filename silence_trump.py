"""
Create a function that takes a string and returns a new string with all vowels removed.
Examples
"I have never seen a thin person drinking Diet Coke." ➞ " hv nvr sn  thn prsn drnkng Dt Ck."

"We're gonna build a wall!" ➞ "W'r gnn bld  wll!"

"Happy Thanksgiving to all--even the haters and losers!" ➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"

"""

import re

def silence_Trump(txt):
    return re.sub("a|e|i|o|u|A|E|I|O|U", "", txt)
