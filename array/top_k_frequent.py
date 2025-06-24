def top_frequent(arr,k):
    hash_map={}
    for i in range(len(arr)):
        hash_map[arr[i]]=1+hash_map.get(arr[i],0)

    result=[]

    for i,j in hash_map.items():
        if j==k:
            result.append(i)

    return result
arr=[1,1,2,2,3]
k=2
print(top_frequent(arr,k))

# for leetcode question
def top_frequent_element(arr,k):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]=1+freq.get(num,0)
        else:
            freq[num]=1

    freq_list=list(freq.items())
    freq_list.sort(key=lambda x:x[1],reverse=True)
    result=[]
    for i in range(k):
        result.append(freq_list[i][0])
    return result

arr=[1,1,2,2,3]
k=2
print(top_frequent_element(arr,k))