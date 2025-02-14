def mergeAlternately( word1, word2):
        arr=[]
        i,j=0,0
        len1,len2=len(word1),len(word2)
        while i <len1 and j<len2:
            arr.append(word1[i])
            arr.append(word2[j])
            i+=1
            j+=1
        if i<len1:
            arr.append(word1[i:])
        if j<len2:
            arr.append(word2[j:])
        return "".join(arr)

s1,s2="rohan","ar"

print(mergeAlternately(s1,s2))