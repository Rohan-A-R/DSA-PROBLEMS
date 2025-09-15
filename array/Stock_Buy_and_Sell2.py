def stock(arr):
    profit=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            current=arr[i]-arr[i-1]
            profit+=current
    return profit



arr=[7, 10, 1, 3, 6, 9, 2]
print(stock(arr))