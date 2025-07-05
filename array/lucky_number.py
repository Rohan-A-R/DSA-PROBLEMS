from collections import Counter

def lucky(arr):
    count=Counter(arr)
    max_no=-1
    for key,value in count.items():
        if key==value:
            max_no=max(max_no,key)
    return max_no

arr=[1,2,2,3,3]
print(lucky(arr))
