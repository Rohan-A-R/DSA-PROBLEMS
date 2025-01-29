# using  hashset

def duplicate(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
arr=[1,2,3,8,7,1]

print(duplicate(arr))

# using sorting
def contains_duplicate_sorting(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return True
    return False

print(contains_duplicate_sorting(arr))