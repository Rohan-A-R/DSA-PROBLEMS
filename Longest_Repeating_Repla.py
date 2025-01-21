def character_replacement(s,k):
    freq={}
    start=0
    max_count=0
    max_length=0
    for end in range(len(s)):
        freq[s[end]]=freq.get(s[end],0)+1
        max_count=max(max_count,freq[s[end]])
        while (end-start+1)-max_count>k:
            freq[s[start]]-=1
            start+=1
        max_length=max(max_length,end-start+1)
    return max_length

s="ABBA"
k=3
print(character_replacement(s,k))
