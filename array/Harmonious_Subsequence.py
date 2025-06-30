# from collections import Counter
def harmonious_sub(arr):
    arr.sort()
    start=0
    max_len=0
    for end in range(len(arr)):
        while arr[end]-arr[start]>1:
            start+=1
        
        if arr[end]-arr[start]==1:
            max_len=max(max_len,end-start+1)
    return max_len

nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(harmonious_sub(nums))

