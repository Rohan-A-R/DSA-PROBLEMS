# brute force
def conscetive_no(arr):
    max_len=1
    for num in arr:
        current=1
        current_num=num
        while (current_num+1) in arr:
            current+=1
            current_num+=1
        max_len=max(current,max_len)

    return max_len

arr = [100, 4, 200, 1, 3, 2]
print(conscetive_no(arr))

# optimal
def optimal(arr):
    if not arr:
        return 0
    current=1
    max_len=1
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            continue
        elif arr[i]==arr[i-1]+1:
            current+=1
        else:
            current=1
        max_len=max(max_len,current)
    return max_len

arr = [100, 4, 200, 1, 3, 2]
print(optimal(arr))