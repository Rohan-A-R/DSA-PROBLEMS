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


def is_palindrome(s):
    s = ''.join(e.lower() for e in s if e.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
    print(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True



s1='ara'
print(is_palindrome(s1))
