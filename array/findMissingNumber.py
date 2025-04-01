# method 1
def findMissingNumber(arr):
    n=len(arr)+1
    total_sum=n*(n+1)//2
    arr_sum=sum(arr)
    return total_sum-arr_sum

arr=[1, 2, 3, 5]
print(findMissingNumber(arr))

# method 2

def find_method(arr):
    n=len(arr)
    while n>=0:
        if n in arr:
            n-=1
        else:
            return n
        
arr=[ 3, 5,6]
print(find_method(arr))


