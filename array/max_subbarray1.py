# brute  force
def brute_force(arr,k):
    max_sum=0
    for i in  range(len(arr)-k+1):
        current_sum=0
        for j in range(k):
            current_sum+=arr[i+j]
        avg=current_sum/k
            
        max_sum=max(max_sum,avg)
    return max_sum

arr=[1,12,-5,-6,50,3]
k=4
print(brute_force(arr,k))

# sliding window
def sliding_window(arr,k):
    current=sum(arr[:k])
    max_sum=current
    for i  in range(k,len(arr)):
        current=current-arr[i-k]+arr[i]
        max_sum=max(current,max_sum)
    return max_sum/k
arr=[5]
k=8
print(sliding_window(arr,k))

