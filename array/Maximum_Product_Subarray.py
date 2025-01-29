# BruteForce
def brute_force(arr):
    n=len(arr)
    max_sub=float('-inf')
    for i in range(n):
        product=1
        for j in range(i,n):
            product=product*arr[j]
            max_sub=max(max_sub,product)
    return max_sub

arr=[-1, -3, -10, 0, 6]
print(brute_force(arr))

# optimal 

def max_product_subarry(arr):
    max_product=arr[0]
    min_product=arr[0]
    result=arr[0]


    for i in range(1,len(arr)):
        num=arr[i]

        if num<0:
            max_product,min_product=min_product,max_product

        max_product=max(num,max_product*num)
        min_product=min(num,min_product*num)

        result=max(result,max_product)
    return result

arr1=[-1]
print(max_product_subarry(arr1))

'''Why do we track both max_product and min_product?
A negative number can become the maximum product when multiplied by 
another negative number.

What if the array contains only one element?
The algorithm works correctly as max_product, min_product, and result
 are initialized to the first element.

How does the algorithm handle zeros?
When encountering a zero, both max_product and min_product reset to 
zero, effectively starting a new subarray.

What is the time complexity of this solution?
Time complexity is 
𝑂(𝑛)
O(n), as the array is traversed once.

Can this algorithm be used for floating-point numbers?
Yes, it works for both integers and floating-point numbers.'''



