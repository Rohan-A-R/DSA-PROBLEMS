class Solution:
    def swapKth( k, arr):
        n=len(arr)
        start=k-1
        end=n-k
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        return arr
    
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
k1 = 3
print(Solution.swapKth(k1,arr1))


