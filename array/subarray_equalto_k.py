# brute force
def subarray_equal_to_k(arr,k):
    count=0
    for i in range(len(arr)):
        sum1=0
        for j in range(i,len(arr)):
            sum1+=arr[j]
            if  sum1==k:
                count+=1
    return count

k=2
arr=[1,1,1]
print(subarray_equal_to_k(arr,k))

# if all numbers are all equal
def subarray_equal_to_k(arr,k):
    sum1=0
    count=0
    low=0
    for high in range(len(arr)):
        sum1+=arr[high]
        if sum1>k and low<=high:
            sum1-=arr[high]
            low+=1
        
        if sum1==k:
            count+=1
    return count

arr=[1, 2, 1, 2, 1]
k=3
print(subarray_equal_to_k(arr,k))