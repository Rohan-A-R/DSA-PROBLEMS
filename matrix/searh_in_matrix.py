def matrix_brute(matrix,target):   

    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==target:
                return True

    return False


arr=[[1,2,3],[4,5,6],[7,8,9]]
target=8

print(matrix_brute(arr,target))

def matrix_search_effcient(arr,target):
    rows=len(arr)
    cols=len(arr[0])
    low=0
    high=rows*cols-1
    while low<=high:
        mid=(low+high)//2
        row=mid//cols
        col=mid%cols
        if arr[row][col]==target:
            return True
        elif arr[row][col]<target:
            low=mid+1
        else:
            high=mid-1

    return False

arr=[[1,2,3],[4,5,6],[7,8,9]]
target=10
print(matrix_search_effcient(arr,target))
