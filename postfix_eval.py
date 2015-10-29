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

def do_math(op1,op2,op):
    op1 = int(op1)
    op2 = int(op2)
    if op == "*":
        return op1 * op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else:
        return op2 / op1
        
def postfix_eval(exp):
    s = Stack()
    input_list = exp.split(' ')
    for i in input_list:
        if i.isdigit():
            s.push(i)
        else:
            op1 = s.pop()
            op2 = s.pop()
            res = do_math(op1,op2,i)
            s.push(res)
            
    return s.pop()
               
        
def main():
    input_exp = raw_input("Expression: ")
    res = postfix_eval(input_exp)
    print(res)
    
    
    
if __name__ == "__main__":main()
