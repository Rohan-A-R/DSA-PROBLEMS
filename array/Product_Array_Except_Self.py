
# this takes o(n)complexity because the value is storing
def Product_Array_Except_Self(arr):
    n=len(arr)
    prefix=[1]*n
    sefix=[1]*n
    res=[1]*n

    for i in range(1,n):
        prefix[i]=prefix[i-1]*arr[i-1]

    for i in range(n-2,-1,-1):
        sefix[i]=sefix[i+1]*arr[i+1]

    for i in range(n):
        res[i]=prefix[i]*sefix[i]

    return res
arr = [10, 3, 5, 6, 2]
print(Product_Array_Except_Self(arr))

# this usin o(1) space 
