def reverse_arrr(arr):
    stack=[]
    for num in arr:
        stack.append(num)
    reversed=[]    
    while stack :
        reversed.append(stack.pop())
    return reversed 



arr=[1,2,3,4,5,6]


print(reverse_arrr(arr))



def equi(arr):
    sum=0
    for i in range(len(arr)):
        




arr=[1,2,0,3]