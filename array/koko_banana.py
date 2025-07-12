import math
def function(arr,k):
    low=1
    high=max(arr)
    answer=high
    while low<=high:
        mid=(low+high)//2
        hours=0
        for pile in arr:
            hours+=math.ceil(pile/mid)
        if hours<=k:
            answer=mid
            high=mid-1
        else:
            low=mid+1

    return answer

arr=[3,11,4,5]
k=11
print(function(arr,k))