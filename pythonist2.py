# 1. Merge the Tools
"""
Given a string S of length N . You have to divide this string into N/K equal parts thus each part contains exactly K elements.
"""

from collections import OrderedDict
line = input()
n = int(input())
split = [line[i:i+n] for i in range(0, len(line), n)]
for i in split:
   print ("".join(OrderedDict.fromkeys(i)))

# 2. Hex Color Code

"""
You are given N lines of CSS code. 
Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
"""

import re
input_string = ""
n = int(input())
for i in range(0,n):
    temp = input()
    input_string= input_string + temp


inside_brackets = re.findall(r'\{.*?\}', input_string, flags=re.DOTALL)
for attributes in inside_brackets:
    lists = re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', attributes)
    for ele in lists:
        print (ele)