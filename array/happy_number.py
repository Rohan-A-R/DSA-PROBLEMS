def happy_number(n):
    seen=set()
    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        sum=0
        for i in str(n):
            sum=sum+int(i)**2
        n=sum
    return True




n=19
print(happy_number(n))

# another method
def happy_another(n):
    while True:
        sum=0
        for i  in str(n):
            sum=sum+int(i)**2
        n=sum
        if n==1:
            return True
        if n in [4, 16, 37, 58, 89, 145, 42, 20]:
            return False
        
n=19
print(happy_another(n))
        