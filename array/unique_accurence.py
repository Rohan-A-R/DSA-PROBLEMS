def unique_accurence(arr):
    hash_map={}
    for num in arr:
        hash_map[num]=1+hash_map.get(num,0)
        
    result=[]
    for i in hash_map.values():
        if i in result:
            return False
        result.append(i)
    return True



arr=[1,1,1,2,2,3,3]
print(unique_accurence(arr))