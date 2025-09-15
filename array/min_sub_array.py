# brute force
def brute_force(arr,target):
    min_sub=float("inf")
    for i in range(len(arr)):
        current=0
        for j in range(i,len(arr)):
            current+=arr[j]
            if current==target:
                min_sub=min(min_sub,j-i+1)
    return min_sub

target = 4
nums = [1,4,4]
print(brute_force(nums,target))



# optimal
def  optimal(arr,target):
    low=0
    total=0
    min_sub=float("inf")
    for high  in range(len(arr)):
        total+=arr[high]
        while total>=target:
            min_sub=min(min_sub,high-low+1)
            total-=arr[low]
            low+=1
    return  min_sub

print(optimal(nums,target))