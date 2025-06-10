def max_diffrence(arr):
    i=0
    j=1
    result=-1
    while j<len(arr):
        if arr[i]<arr[j]:
            sum1=arr[j]-arr[i]
            result=max(sum1,result)
            j+=1

        else:
            i=j
            j+=1

    return result

print(max_diffrence([2,1,3,4,5,7]))
