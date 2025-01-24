def reverse(arr):
    result=[]
    for i in range(len(arr)):
        result.insert(0,arr[i])
    return result


arr=[1,2,3,4,5,6,7,8]

print(reverse(arr))