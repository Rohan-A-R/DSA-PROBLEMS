# Bruteforce 
def brute_3summ(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]==target:
                    return True
    return False


arr=[40, 20, 10, 3, 6, 7]
target=24
print(brute_3summ(arr,target))

# using hashset
def hash_3sum(arr,target):
    for i in range(len(arr)):
        seen=set()
        complement=target-arr[i]
        for j in range(i+1,len(arr)):
            if complement-arr[j] in seen:
                return True
            seen.add(arr[j])
    return False


arr1=[1, 4, 45, 6, 10, 8]
target1=13
print(hash_3sum(arr1,target1))
