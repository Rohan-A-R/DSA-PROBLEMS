def search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[10,20,14,17,16]
target=int(input('enter the num'))

print(search(arr,target))