def array_leades(arr):
    leader=[]
    max_number=arr[-1]
    leader.append(max_number)
    n=len(arr)
    for i in range(n-2,-1,-1):
        if arr[i]>=max_number:
            leader.append(arr[i])
            max_number=arr[i]
    return leader[::-1]

arr = [16, 17, 4, 3, 5, 2]
print(array_leades(arr))