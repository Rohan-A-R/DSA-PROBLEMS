def second_largest(arr):
    largest = sec =-1
    for num in arr:
        if num > largest:
            sec=largest
            largest=num
        elif num > sec and num != largest:
            sec=num
    return sec

arr= [12, 35, 1, 10, 34, 1]
            
print(second_largest(arr))