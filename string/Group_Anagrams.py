def group_anagrams(arr):
    hash_map={}
    for word in arr:
        freq=[0]*26
        for char in word:
            freq[ord(char)-ord('a')]+=1
        key=tuple(freq)

        if key not in hash_map:
            hash_map[key]=[]
        hash_map[key].append(word)

    return list(hash_map.values())

arr=["act", "god", "cat", "dog", "tac"]
print(group_anagrams(arr))


        

