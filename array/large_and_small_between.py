def in_between(arr):
    arr.sort()
    left=0
    right=len(arr)-1
    result=[]
    while left <=right:
        if left!=right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[right])

        left+=1
        right-=1
    return result


arr=[2,4,6,1,8,5]

print(in_between(arr))
