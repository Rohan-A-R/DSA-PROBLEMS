# brute force 
def function(string):
    count=0
    i=len(string)-1
    while i>=0 and string[i]==' ':
        i-=1

    while i>=0 and string[i]!=' ':
        count+=1
        i-=1
    
    return count

s="hello rohan     "
print(function(s))

# optimal
def optimal(s):
    arr=s.split()
    n=len(arr)
    return len(arr[n-1])
s="hello rohanaaaa"
print(optimal(s))