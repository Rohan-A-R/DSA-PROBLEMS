def equlibrim(arr):
    total=sum(arr)
    left=0
    for i in range(len(arr)):
        right=total-left-arr[i]
        if left==right:
            return i
        left+=arr[i]
    return -1



def equi(arr):
    for i in  range(len(arr)):
        left=sum(arr[:i])
        right=sum(arr[i+1:])
        if left==right:
            return i
        
    return -1






arr=[1,7,3,6,5,6]

print(equlibrim(arr))