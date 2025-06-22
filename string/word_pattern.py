# brute force
def  word_pattern(pattern,s):
    word=s.split()
    if len(pattern)!=len(word):
        return False
    
    for i in range(len(pattern)):
        if pattern.index(pattern[i])!=word.index(word[i]):
            return False
        
    return True


pattern = "abba"
s = "dog cat cat og"
print(word_pattern(pattern,s))


# using hash
def  word_pattern(pattern,s):
        word=s.split()
        if len(pattern)!=len(word):
            return False
        patt_word={}
        word_patt={}
        for i in range(len(pattern)):
            pt=pattern[i]
            ch=word[i]
            if  pt in patt_word:
                if patt_word[pt]!=ch:
                    return False
            else:

                if ch in word_patt:
                    return False
                patt_word[pt]=ch
                word_patt[ch]=pt

        return True

pattern = "abba"
s = "dog cat cat dog"
print(word_pattern(pattern,s))