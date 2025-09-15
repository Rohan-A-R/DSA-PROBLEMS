def brute_force(x):
    if x==0:
        return x
    for i in range(x+1):
        if i**2==x:
            return i
        if i**2>x:
            return i-1
        
x=4
print(brute_force(x))
            