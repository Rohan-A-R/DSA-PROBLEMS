class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        self.toselfp=None
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.top is None:
            return -1
        popped_value=self.top.value
        self.top=self.top.next
        return popped_value
        
    def peek(self):
        if self.top is None:
            return -1
        return self.top.value
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        current=self.top
        while current:
            print(current.value,end=" -> ")
            current=current.next
        print("None")
