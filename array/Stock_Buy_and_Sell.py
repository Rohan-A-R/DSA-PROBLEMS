def maximumProfit(arr):
        left,right=0,0
        res=0
        while right<len(arr):
            if arr[left]<arr[right]:
                total=arr[right]-arr[left]
                res=max(res,total)
            else:
                left=right
            right+=1
        return res

arr=[7, 10, 1, 3, 6, 9, 2]

print(maximumProfit(arr))
            