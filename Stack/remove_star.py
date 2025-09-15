def star(s): 
        stack=[]
        for num in s:
            if num=="*":
                stack.pop()
            else:
                stack.append(num)
        return ''.join(stack)

s = "leet**cod*e"
print(star(s))
        
