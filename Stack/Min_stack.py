class Solution:
    def __init__(self):
        self.stack=[]
        self.min=[]

    def push(self,data):
        self.stack.append(data)
        if not self.min or data <=self.min[-1]:
            self.min.append(data)

    def pop(self):
        if self.min:
            popped=self.min.pop
            if popped==self.min[-1]:
                self.min.pop()

    def getmin(self):
        if self.min:
            return self.min[-1]
        return None

