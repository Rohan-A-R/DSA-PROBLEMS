from collections import Counter

def max_subsequence(arr,k):
    sorted_list=sorted(arr,reverse=True)[:k]
    count=Counter(sorted_list)
    result=[]
    for num in arr:
        if count[num]>0:
            result.append(num)
            count[num]-=1
        if len(result)==k:
            break
    return result




print(max_subsequence([2, 1, 3, 3], 2))   # [3, 3]
print(max_subsequence([-1, -2, 3, 4], 3)) # [-1, 3, 4]
print(max_subsequence([3, 4, 3, 3], 2))   # [3, 4]
