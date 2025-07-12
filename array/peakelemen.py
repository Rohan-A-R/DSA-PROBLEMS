def function(arr):        
        low=0
        high=len(arr)-1
        while low<high:
            mid=(low+high)//2
            if arr[mid]>arr[mid+1]:
                high=mid
            else:
                low=mid+1
        return low

arr=[1,3,2,1]
print(function(arr))