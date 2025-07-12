def brute_force(arr,target):
    new=[]
    for i in range(len(arr)):
        if arr[i]==target:
            new.append(i)
            break
    j=len(arr)-1
    for num in arr[::-1]:
        if num==target:
            new.append(j)
            return new
        else:
            j-=1
    return [-1,-1]

arr=[]
Target=1
print(brute_force(arr,Target))