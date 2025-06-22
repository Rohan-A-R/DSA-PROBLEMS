def contains_duplicate(arr,k):
    seen=set()
    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        seen.add(arr[i])

        if len(seen)>k:
            seen.remove(arr[i-k])

    return False


nums = [1,2,3,1]
k = 3
print(contains_duplicate(nums,k))