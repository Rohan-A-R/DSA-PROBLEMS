def min_number(arr,low,high):
    n=len(arr)
    low=0
    high=n-1
    res=arr[0]

    while low <=high:
        if arr[low]<arr[high]:
            res=min(res,arr[low])
            break
        mid=(low+high)/2
        res=min(res,arr[mid])
        if arr[mid]>=arr[low]:
            low=mid+1
        else:
            high=mid-1

    return res





         

