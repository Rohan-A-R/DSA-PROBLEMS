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



def prefix_equi(arr):
    prefix=[0]*len(arr)
    suffif=[0]*len(arr)
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i-1]
    for  i in range(len(arr)-2,-1,-1):
        suffif[i]=suffif[i+1]+arr[i+1]
    for i in range(len(arr)):
        if prefix[i]==suffif[i]:
            return i
    return -1
        
    
arr=[1,7,3,6,5,6]
print(prefix_equi(arr))

print(equlibrim(arr))