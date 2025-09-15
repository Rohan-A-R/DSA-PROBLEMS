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

from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)  # Dictionary to hold grouped anagrams
    print(anagram_map.items())

    for word in words:
        sorted_word = ''.join(sorted(word))  # Sort letters in the word
        print(sorted_word)
        anagram_map[sorted_word].append(word)  # Group by sorted word

    return list(anagram_map.values())  # Return only the grouped values

# Example usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)


        

