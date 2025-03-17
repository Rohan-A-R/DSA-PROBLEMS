# class Solution:
#     def __init__(self):
#         self.stack=[]
#         self.min=[]

#     def push(self,data):
#         self.stack.append(data)
#         if not self.min or data <=self.min[-1]:
#             self.min.append(data)

#     def pop(self):
#         if self.min:
#             popped=self.min.pop()
#             if popped==self.min[-1]:
#                 self.min.pop()

#     def getmin(self):
#         if self.min:
#             return self.min[-1]
#         return None

def deleteMid(stack):
    def helper(stack, current, mid):
        # Base case: If we reached the middle, remove the element
        if current == mid:
            stack.pop()
            return
        
        # Remove the top element
        temp = stack.pop()

        # Recursive call for the remaining elements
        helper(stack, current + 1, mid)

        # Push the element back after the middle one is removed
        stack.append(temp)

    # Calculate middle index (0-based index)
    mid = len(stack) // 2

    # Start recursion from index 0
    helper(stack, 0, mid)

    return stack  # Return modified stack (optional)

# Example Usage:
s = [10, 20, 30, 40, 50]
print(deleteMid(s))  # Ou



s = [10, 20, 30, 40, 50]
print(deleteMid(s))