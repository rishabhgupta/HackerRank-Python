# -*- coding: utf-8 -*-
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

def python_way(input_str):
    right = input_str.count('(')
    left = input_str.count(')')
    print True if right == left else False
    
def stack_way(input_str):
    balance = True
    s = Stack()
    for c in input_str:
        if c == '(':
            s.push(c)
        else:
            if s.is_empty():
                balance = False
                break
            else:
                s.pop()
                
    print True if balance and s.is_empty() else False
                
def matches(char1, char2):
    open_set, close_set = '[{(', ']})'
    return True if open_set.index(char1) == close_set.index(char2) else False

def general_stack(input_str):
    balance = True
    s = Stack()
    for c in input_str:
        if c in "[{(":
            s.push(c)
        else:
            if s.is_empty():
                balance = False
                break
            else:
                top = s.pop()
                if not matches(top,c):
                    balance = False
                    break
    
    print True if balance and s.is_empty() else False
    
def main():
    input_string = raw_input("Enter String: ")
    general_stack(input_string)
                    
if __name__ == "__main__":main()
