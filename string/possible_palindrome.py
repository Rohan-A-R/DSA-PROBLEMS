from collections import Counter
def longest(arr):
    hash_map=Counter(arr)
    count=0
    odd=0
    for num in hash_map.values():
        count+=(num//2)*2
        if num%2==1:
            odd+=1

    if odd>0:
        count+=1

    return count

s = "abccccdd"
print(longest(s))