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




def quicksort(arr,low,high):
    if low<high:
        pivot_index=partition(arr,low,high)  
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)
        

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

arr=[2,5,3,2,5,7,9,7,5]
quicksort(arr,0,len(arr)-1)

print(arr)