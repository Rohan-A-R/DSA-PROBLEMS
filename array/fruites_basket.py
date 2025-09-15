# brute force
def brute_force(arr):
    max_len=0
    for i in range(len(arr)):
        hash_set=set()
        for j in range(i,len(arr)):
            hash_set.add(arr[j])
            if len(hash_set)>2:
                break
        max_len=max(max_len,j-i+1)
    return max_len

arr1=[3,3,3,1,2,1,1,2,3,3,4]
arr=[1,2,1]
print(brute_force(arr))

from collections import defaultdict

def optimal(arr):
    count=defaultdict(int)
    max_sub=0
    left=0
    for high in range(len(arr)):
        count[arr[high]]+=1
        while len(count)>2:
            count[arr[left]]-=1
            if count[arr[left]]==0:
                del count[arr[left]]
            left+=1
        max_sub=max(max_sub,high-left+1)
    return max_sub

print(optimal(arr1))