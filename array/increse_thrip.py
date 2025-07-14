# brutefrce
def brute_force(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]<arr[j]<arr[k]:
                    return True
    return False

nums = [1,2,3,4,5]
print(brute_force(nums))


# optimal
def optimal(arr):
    first=float('-inf')
    second=float('-inf')
    for num in arr:
        if num <=first:
            first=num
        elif num<second:
            second=num
        else:
            return True
    return False

nums =[5,4,3,2,1]
print(optimal(nums))
