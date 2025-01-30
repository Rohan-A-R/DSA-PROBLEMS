def string_rotate(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    left_roted=s1[2:]+s1[:2]
    right_roted=s1[-2:]+s1[:-2]
    return s2==left_roted or s2==right_roted 


s1="amazon"
s2="azonam"
print(string_rotate(s1,s2))