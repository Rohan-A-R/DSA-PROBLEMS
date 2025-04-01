def array_subset(m,n):
    set_a=set(m)
    for elem in n:
        if elem not in set_a:
            return False
    return True

a = [11, 7, 1, 13, 21, 3, 7, 3] 
b= [11, 3, 7, 1, 7]
print(array_subset(a,b))
