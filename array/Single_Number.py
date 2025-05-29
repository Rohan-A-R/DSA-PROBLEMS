def single_number(arr):
    hash_map={}
    for num in arr:
        hash_map[num]=hash_map.get(num,0)+1
    for key ,value in hash_map.items():
        if value ==1:
            return key
        

arr=[1,1,2,2,3,3,4]
print(single_number(arr))