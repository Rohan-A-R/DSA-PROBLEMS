def isIsomorphic(s,t):
        if len(s)!=len(t):
            return False

        hash1={}
        hash2={}
        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if c1 in hash1:
                if hash1[c1]!=c2:
                    return False

            else:
                hash1[c1]=c2

            if c2 in hash2:
                if hash2[c2]!=c1:
                    return False

            else:
                hash2[c2]=c1

        return True


print(isIsomorphic('roo','add'))