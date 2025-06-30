def kidsWithCandies(arr,n):
        max_no=max(arr)
        arr1=[]
        for i in range(len(arr)):
            if arr[i]+n<max_no:
                arr1.append(False)
            else:
                arr1.append(True)

        return arr1
arr=[2,3,5,1,3] 
n=3
print(kidsWithCandies(arr,n))
        

def maping(arr,n):
     max_no=max(arr)
     return [num+n >=max_no for num in arr ]

print(maping(arr,n))