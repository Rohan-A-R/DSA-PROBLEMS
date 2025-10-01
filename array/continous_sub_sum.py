def sub_arr_sum(arr,k):
    for i in range(len(arr)):
        sum1=0
        for j in range(i,len(arr)):
            sum1+=arr[j]
            if j-i+1>=2 and sum1%k==0:
                return True
    return False


arr=[23,2,4,6,7]
k=6
print(sub_arr_sum(arr,k))

# optimal using hashmap
def sub_arr_sum1(arr,k):
    hash_map={0:-1}
    prefix_sum=0
    for i,num in enumerate(arr):
        print(hash_map)
        prefix_sum+=num
        rem=prefix_sum%k
        if rem in hash_map:
            if i-hash_map[rem]>2:
                return True
        else :
            hash_map[rem]=i
    return False
arr=[23,2,4,6,7]
k=6
print(sub_arr_sum1(arr,k))
        

