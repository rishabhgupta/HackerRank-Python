# -*- coding: utf-8 -*-

from __future__ import print_function

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    
def main():
    input_exp = raw_input("Expression: ")
    input_list = input_exp.split(' ')
    
    rank = {}
    rank["*"]=3
    rank["/"]=3
    rank["+"]=2
    rank["-"]=2
    rank["("]=1
    
    output_list = []
    s = Stack()
    for i in input_list:
        if i.isalpha():
            output_list.append(i)
        elif i in "(+-*/":
            while not s.is_empty() and s.peek() in "(+-*/" and rank[s.peek()]>=rank[i]:
               top = s.pop()
               output_list.append(top)
            s.push(i)
        elif i == ')':
            while s.peek()!='(' and not s.is_empty():
                top = s.pop()
                output_list.append(top)
            s.pop()
    
    while not s.is_empty():
        top = s.pop()
        output_list.append(top)
    
    for i in output_list: 
        print(i,end="")
    
    
if __name__ == "__main__":main()
