

def longest_palindromic(s):
    def is_palindrom(s,left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    n=len(s)
    max_len=0
    result=""
    for i  in range(n):
        for j in range(i,n):
           if is_palindrom(s,i,j) and (j-i+1)>max_len:
            max_len=j-i+1
            result=s[i:j+1]
    return result



s="aaaabbaa"
print(longest_palindromic(s))

