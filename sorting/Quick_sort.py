def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivote=arr[len(arr)//2]

    left =[x for x in arr if x < pivote]
    middle=[x for x in arr if x==pivote]
    right=[x for x in arr if x > pivote]

    return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5,34,657,86,]
print( quick_sort(arr))
