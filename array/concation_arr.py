def concatiation(arr):
    n=len(arr)
    arr1=[0]*(2*n)
    for i in range(n):
        arr1[i]=arr[i]
        arr1[i+n]=arr[i]
    return arr1



print(concatiation([1,2,3,4]))