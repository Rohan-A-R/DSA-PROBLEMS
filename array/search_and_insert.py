def search_and_insert(arr,target):
    low,high=0,len(arr)-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low

arr=[1,5,8,9,15,17,18,21,25]
target=17

print(search_and_insert(arr,target))

