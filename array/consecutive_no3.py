def optimal(arr,k):
    low=0
    current=0
    max_no=0
    for high in range(len(arr)):
        if arr[high]==0:
            current+=1

        while current>k:
            if arr[low]==0:
                current-=1
            low+=1
        max_no=max(max_no,high-low+1)

    return  max_no

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(optimal(nums,k))