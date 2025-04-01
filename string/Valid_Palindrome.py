def valid_palindrome(s):
    filtered_chars=[]
    for char in s:
        if char.isalnum():
            filtered_chars.append(char.lower())
    s=''.join(filtered_chars)

    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True


s = "ara"
print(valid_palindrome(s))