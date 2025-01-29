def valueEqualsIndex(arr):
    result=[]
    for i in range(len(arr)):
        if  arr[i]==i+1:
            result.append(i+1)
    return result