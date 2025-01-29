def Maximum_Subarray(arr):
    current_sum=0
    max_sum=float('-inf')
    for num in arr:
        if current_sum+num>num:
            current_sum+=num
        else: 
            current_sum=num

        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum

arr1 = [2, 3, -8, 7, -1, 2, 3]
print(Maximum_Subarray(arr1))



# using inbuilt
def inbuilt(arr):
    current_sum=0
    max_sum=float('-inf')

    for i in range(len(arr)):
        current_sum=current_sum+arr[i]
        max_sum=max(max_sum,current_sum)

        if current_sum<0:
            current_sum=0

    return  max_sum

arr1 = [2, 3, -8, 7, -1, 2, 3]
print(inbuilt(arr1))


# more
def kadane(arr):
    # Initializing the variables
    current_sum = 0
    max_sum = float('-inf')
    
    for num in arr:
        current_sum = max(num, current_sum + num)  # Either start new subarray or extend the current subarray
        max_sum = max(max_sum, current_sum)  # Update the max sum if current_sum is greater
        
    return max_sum
