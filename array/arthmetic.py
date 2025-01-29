class Solution:
    def canFormAP(self, arr):
        # Sort the array
        arr.sort()

        arr_dif=arr[1]-arr[0]

        for i in range(2,len(arr)):
            if arr[i]-arr[i-1] != arr_dif:
                return False
        return True
    

arr1 = [0, 12, 4, 8,6]
solution = Solution()
print(solution.canFormAP(arr1))