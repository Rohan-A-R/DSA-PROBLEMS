def index_subarr(arr,target):
    sum1=0
    low=0
    for high in range(len(arr)):
        sum1+=arr[high]
        while sum1>target and low<high:
            sum1-=arr[low]
            low+=1
        if sum1==target:
            return [low+1,high+1]
    return [-1]


arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=15
print(index_subarr(arr,target))