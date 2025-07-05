class Solution:
	def common_digits(self, nums):
		digit=set()
		for i in str(nums):
			digit.add(int(i))
		return digit
	
sol = Solution()
nums1 = [131, 11, 48]
print(sol.common_digits(nums1))
				