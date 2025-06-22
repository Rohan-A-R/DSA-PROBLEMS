# bruit force

def max_3_no_product(arr):
    n=len(arr)
    max_product=float("-inf")
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                product=arr[i]*arr[j]*arr[k]
                max_product=max(product,max_product)
    return max_product


arr=[1,2,3,4,5]
print(max_3_no_product(arr))


# optimal solution

def max_3_no_product_optimal(arr):
    max1=max2=max3=float("-inf")
    min1=min2=float("inf")
    for num in arr:
        if num >max1:
            max1,max2,max3=num,max1,max2
        elif num>max2:
            max2,max3=num,max2
        elif num>max3:
            max3=num

        if num < min1:
            min1,min2=num,min1

        elif num<min2:
            min2=num
    
    return max(max1*max2*max3,max1*min1*min2)

arr=[1,2,3,4,5]
print(max_3_no_product_optimal(arr))

