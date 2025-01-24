# first Method
def reverse_string(s):
    arr=[]
    for  i in s:
        arr.insert(0,i)
    return "".join(arr)

s="rohan"

print(reverse_string(s))

# second method 2 pointer
def reverse_string_method1(s):
    l,r=0,len(s)-1
    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return s
s = ["h","e","l","l","o"]
print(reverse_string_method1(s))


