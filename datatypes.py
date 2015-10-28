# 1. LISTS

"""
You have to initialize your list L = [] and follow the N commands given in N lines.
"""

arr = []
n = input()

for i in range(int(n)):
    input_str = input()
    split_str = input_str.split(' ')
    if split_str[0] == 'insert':
        arr.insert(int(split_str[1]),int(split_str[2]))
    elif split_str[0] == 'print':
        print(arr)
    elif split_str[0] == 'remove':
        arr.remove(int(split_str[1]))
    elif split_str[0] == 'append':
        arr.append(int(split_str[1]))
    elif split_str[0] == 'sort':
        arr.sort()
    elif split_str[0] == 'reverse':
        arr.reverse()
    elif split_str[0] == 'pop':
        arr.pop()
        
# 2. TUPLES

"""
You are given an integer N in one line. The next line contains N space-separated integers. Create a tuple of those N integers. Lets call it T. 
Compute hash(T) and print it.
"""

n = input()
input_str = input()
lst_int = [int(x) for x in input_str.split(" ")]
tup = tuple(lst_int)
print(hash(tup))

# 3. SETS - SYMMETRIC DIFFERENCE 

"""
Given two set of integers M and N and print their symmetric difference in ascending order. 
"""

N = int(input())
int_list1 = list(map(int,input().split()))
N = int(input())
int_list2 = list(map(int,input().split()))

setA = set(int_list1)
setB = set(int_list2)

setADB = setA.difference(setB)
setBDA = setB.difference(setA)

res = []
for i in setADB:
    res.append(i)
    
for i in setBDA:
    res.append(i)

res.sort()

for i in res:
    print(i)

# List Comprehensions
"""
Given three integers X, Y and Z denoting the dimensions of a Cuboid. 
Print a list of all possible coordinates on the three dimensional grid...
"""
x, y, z, n = (int(input()) for _ in range(4))
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n ])

# Find second largest number in a list

num, input_list = int(input()), [int(x) for x in input().split(' ')]
l = list(set(input_list))
l.sort()
print(l[-2])

# Nested list

"""
There is a classroom of 'n' students and you are given their names and marks in physics. 
Print the name of each student who got the second lowest marks in physics.
"""
num = int(input())
complete_list = [[input(), float(input())] for _ in range(num)]
complete_list.sort(key=lambda x: x[1])
marks_sorted = sorted({mark[1] for mark in complete_list})
result = sorted(value[0] for value in complete_list if value[1]==marks_sorted[1])
for name in result:
    print(name)