def move_zero(arr):
    start=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[start]=arr[start],arr[i]
            start+=1
    return arr


arr=[1,0,3,0,4,6,0,8,0,0]

print(move_zero(arr))