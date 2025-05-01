def string(arr,target):
    for i  in range(len(arr)):
        if arr[i]==target:
            return i
    return False

arr='rohan is good'
target=str(input('enter the string'))

print(string(arr,target))