def function(string1,string2):
    hash_map={}
    for num in string2:
        hash_map[num]=1+hash_map.get(num,0)
    for num1 in string1:
        if num1 in hash_map and hash_map[num1]>0:
            hash_map[num1]-=1
        else:
            return False
    return True

s1="aabb"
s2="abaabbb"
print(function(s1,s2))


    