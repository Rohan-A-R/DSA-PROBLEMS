def brute_force(s1,s2):
        if len(s1)>len(s2):
            return False

        arr = sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            window=s2[i:i+len(s1)]
            if sorted(window)==arr:
                return True

        return False

s1 = "abz"
s2 = "eidbaooo"
print(brute_force(s1,s2))

# optimal
from collections import Counter
def optimal(s1,s2):
    s1_len=len(s1)
    s2_len=len(s2)
    if s1_len>s2_len:
         return False

    s1_hash=Counter(s1)
    s2_hash=Counter(s2[:s1_len])

    if s1_hash==s2_hash:
         return True

    for i in range(s1_len,s2_len):
         start=s2[i-s1_len]
         end=s2[i]
         s2_hash[end]+=1
         s2_hash[start]-=1
         

         if s2_hash[start]==0:
              del s2_hash[start]
         if  s1_hash==s2_hash:
              return True
         
    return False
         
s1 = "ab"
s2 = "eidbaooo" 
print(optimal(s1,s2))    