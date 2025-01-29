# Rotating an Array
def rotate(arr,d):
    n = len(arr)
    d %= n  
    return arr[d:] + arr[:d]

arr=  [7, 3, 9, 1]
d = 3
print(rotate(arr,d))  

# Rotating an Array INplace


def rotate_inplace(arr,d):
    n=len(arr)
    d%=n
    def helper_inplace(subarr,start,end):
        while start < end:
            subarr[start],subarr[end]=subarr[end],subarr[start]
            start+=1
            end-=1
    helper_inplace(arr,0,d-1)
    helper_inplace(arr,d,n-1)
    helper_inplace(arr,0,n-1)

    return arr
    
arr1=  [7, 3, 9, 1]
d1 = 2


print(rotate_inplace(arr1,d1))
    
