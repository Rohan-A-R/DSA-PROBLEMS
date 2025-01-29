class Solution:
    def _sum(arr):
           count=0
           for i in arr:
               count+=i
           return count

arr=[1,2,3,6,4,5,8]

print(Solution._sum(arr)) 