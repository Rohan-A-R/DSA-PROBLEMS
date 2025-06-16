def remove_elemenr(arr,value):
    count=0
    for i in range(len(arr)):
        if arr[i]==value:
            count+=1
    return len(arr)-count

arr=[1,2,1,3,4,1]
print(remove_elemenr(arr,1))


def remove_elementarr(arr,value):
    i=0
    while i<len(arr):
        if arr[i]==value:
            arr.pop(i)
        else:
            i+=1
    return arr

arr=[1,2,1,3,4,1]
print(remove_elementarr(arr,1))


# inpalce
def inplace(arr,val):
    k=0
    for i in range(len(arr)):
        if arr[i]!=val:
            arr[k]=arr[i]
            k+=1
    return k

