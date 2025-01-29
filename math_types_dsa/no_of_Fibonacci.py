def no_of_fibonacci_in_arr(arr):
    if not arr:
        False
    max_value=max(arr)
    fib_set=set()
    a,b=0,1
    while a <=max_value:
        fib_set.add(a)
        a,b=b,a+b
    count=0
    for num in arr:
        if num in fib_set:
            count+=1
    return count

arr1 = [4, 2, 8, 5, 20, 1, 40, 13, 23]
print(no_of_fibonacci_in_arr(arr1))
