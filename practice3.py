def stack(arr):
    result=[]
    for i in range(1,6):
        result.append(arr[5-i])
        
    for j in range(5,len(arr)):
        result.append(arr[j])
    
    return result
arr=[50, 40, 30, 20, 10, 60, 70]

print(stack(arr))