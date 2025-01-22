def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]  
        j=i-1       
        while j>=0 and key< arr[j]:
                    
            arr[j+1]=arr[j]
            j=j-1
        
        arr[j+1]=key


arr=[10,5,2,19,4,20]
insertion(arr)
print(arr) 