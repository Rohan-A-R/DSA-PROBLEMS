class MyStack:
    def __init__(self):
        self.q=[]

    def push(self,x):
        self.q.append(x)

        for _ in range(len(self.q)-1):
            self.q.append(self.q.pop(0))

    def pop(self):
        if not  self.empty():
            return self.q.pop(0)
        return -1
    
    def top(self):
        if not self.empty():
            return self.q[0]  
        return -1

    def empty(self): 
        return len(self.q) == 0  
    

from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int):
        self.q.append(x)  # Add new element
        for _ in range(len(self.q) - 1):  
            self.q.append(self.q.popleft())  # Rotate queue to make x front

    def pop(self) -> int:
        return self.q.popleft()  # Remove front element (LIFO behavior)

    def top(self) -> int:
        return self.q[0]  # Peek the front element

    def empty(self) -> bool:
        return len(self.q) == 0  # Check if queue is empty



    
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False
print(stack.pop())  # Output: 1
print(stack.empty())