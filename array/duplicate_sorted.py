def duplicate(nums):    
        if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k+=1
        print(nums)
        return len(set(nums))

arr=[1,1,1,2,2,3,3,4,4]
print(duplicate(arr))
        