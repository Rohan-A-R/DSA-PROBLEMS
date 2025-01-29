# brute froce

def Container_With_Most_Water_brute(arr):
    res=0
    n=len(arr)
    for  i in range(n):
        for j in range(i+1,n):
            area=(j-i)*min(arr[i],arr[j])
            res=max(res,area)
    return res


arr=[1, 5, 4, 3]
print(Container_With_Most_Water_brute(arr))


# optimal
def Container_With_Most_Water_optimal(arr):
    n=len(arr)
    res=0
    left=0
    right=n-1
    while  left<right:
        area=(right-left)*min(arr[left],arr[right])
        res=max(res,area)
        if arr[left] <arr[right]:
            left+=1
        else:
            right-=1
    return res


arr1=[1, 5, 4, 3]
print(Container_With_Most_Water_optimal(arr1))

        