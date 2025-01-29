# 1. Find the Largest Element in an Array
# def largest(arr):
#     largest1=-1
#     for num in arr:
#         if num > largest1:
#             largest1=num
#     return largest1

# arr= [1, 8, 100, 7, 56, 90,120]

# print(largest(arr))

# 2. Reverse an Array

# def reverse(arr):
#     result=[]
#     for num in range(len(arr)):
#         result.insert(0,arr[num])
        
#     return result

# arr=[1,2,3,4,5,6,7,8,9,10]

# print(reverse(arr))

# 3. Check if an Array is Sorted

# def sort(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#     return True
        


# arr=[1, 2,5, 3, 4]

# print(sort(arr))

# 4. Find the Minimum Element in an Array

def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case
print(factorial(5))

