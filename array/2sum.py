# Brute Force
def two_sum(arr,target):
    for i in range(len(arr)):
        for  j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return True
    return False


arr=[16]
target=16
print(two_sum(arr,target))

# 2 pointers

def two_sum_pointer(arr,target):
    arr.sort()
    low,high=0,len(arr)-1
    while low < high:
        current_sum=arr[low]+arr[high]
        if current_sum==target:
            return True
        elif current_sum < target:
            low+=1
        else:
            high-=1
    return False

arr1=[1,8,5,7,6,11,22,4]
target1=27
print(two_sum_pointer(arr1,target1))

# using hash set

def hash_set(arr,target2):
    seen =set()
    for num in arr:
        complement= target2-num
        if complement in seen:
            return True
        seen.add(num)
    return False

arr2=[1,8,5,7,6,11,22,4,18,25,49,40,20]
target2=9

print(hash_set(arr2,target2))

