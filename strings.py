# 1. sWAP cASE

string_input = input()
print(string_input.swapcase())

# 2. String Split and Join

"""
Split the string on " " (space) delimiter and join using a - hyphen.
"""

print ("-".join(input().split(' ')))

# 3. Mutations

"""
Read a string. change the character at a given index and print the string.
"""

input_string = input()
input_list = input().split(' ')
input_string = input_string[:int(input_list[0])] + input_list[1] + input_string[int(input_list[0])+1:]
print(input_string)

# 4. Find a string

"""
Print the number of times that substring occurs in that string
"""
input_str = input()
sub = input()
i, l, count = 0,len(sub),0
while(i<len(input_str)):
    if input_str[i:i+l] == sub:
        count = count +1
    i=i+1;
    
print(count)

# 5. String Validators

"""
Find if string S contains, alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""

str_list = list(raw_input().strip('\n'))
alpha_num, alpha_car, digits, lowcar, upcar = 0, 0, 0, 0, 0
for ch in str_list:
    if ch.isalnum():
        alpha_num += 1
    if ch.isalpha():
        alpha_car += 1
    if ch.isdigit():
        digits += 1
    if ch.islower():
        lowcar +=1
    if ch.isupper():
        upcar +=1

print True if alpha_num else False
print True if alpha_car else False
print True if digits else False
print True if lowcar else False
print True if upcar else False

# 6. Text Alignment

"""
HackerRank Logo of variable thickness. 
"""


thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)    

# 7. Textwrap

import textwrap
str_input = raw_input().strip('\n')
num = int(raw_input())
print textwrap.fill(str_input,num)

# 8. Designer Door Mat

N, M = map(int,input().split()) 
for i in range(1,N,2): 
    print ((".|."*i).center(M,'-'))
print (("WELCOME").center(M,'-'))
for i in range(N-2,-1,-2): 
    print ((".|."*i).center(M,'-'))
