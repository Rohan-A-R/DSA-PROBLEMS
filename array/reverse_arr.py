def reverse(arr):
    result=[]
    for i in range(len(arr)):
        result.insert(0,arr[i])
    return result


arr=[1,2,3,4,5,6,7,8]

print(reverse(arr))


def arr_reverse(arr):
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr

arr=[1,2,3,4,5,6,7,8]
print(arr_reverse(arr))