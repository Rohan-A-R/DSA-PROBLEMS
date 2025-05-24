# method 1
def findMissingNumber(arr):
    n=len(arr)+1
    total_sum=n*(n+1)//2
    arr_sum=sum(arr)
    return total_sum-arr_sum

arr=[ 1,2, 3,4, 5,6,7,8,9,11,12]
print(findMissingNumber(arr))

# method 2

def findMissingNumber_Set(arr):
    n = len(arr) + 1
    nums_set = set(arr)
    
    for i in range(1, n + 1):
        if i not in nums_set:
            return i




