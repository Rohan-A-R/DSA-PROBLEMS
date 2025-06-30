def three_sum(arr):
    seen=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]==0:
                    triplet=tuple(sorted([arr[i],arr[j],arr[k]]))
                    seen.add(triplet)

    return  [list(triplet) for triplet in seen]

arr=[-1, 0, 1, 2, -1, -4]
print(three_sum(arr))


# optimal
def three_sum_optimal(arr):
    arr.sort()
    result=[]
    for i in range(len(arr)-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        low,high=i+1,len(arr)-1
        while low<high:
            total=arr[i]+arr[low]+arr[high]
            if total==0:
                result.append([arr[i],arr[low],arr[high]])
                while low<high and arr[low]==arr[low+1]:
                    low+=1
                while low<high and arr[high]==arr[high-1]:
                    high-=1
                low+=1
                high-=1
            elif total<0:
                low+=1
            else :
                high-=1
    return result

nums = [-1,0,1,2,-1,-4]
print(three_sum_optimal(arr))