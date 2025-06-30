# Iterative Implementation

def gcd(a,b):
    while b !=0:
        a,b=b,a%b
    return a


print(gcd(56,98))


# recursive approch

def gcd1(a,b):
    if b==0:
        return a
    return gcd1(b,a%b)


print(gcd1(56,98))


# full program

def full_gcd(n):
    divseor=[]
    for i in range(1,n+1):
        if n%i==0:
            divseor.append(i)
    return divseor

def gcd3(a,b):
    divisior_a=full_gcd(a)
    divisior_b=full_gcd(b)

    common_divisior=list(set(divisior_a)& set(divisior_b))
    gcd =max(common_divisior)
    return gcd

print(gcd3(56,98))


# Gcd for an array


def find_arr(arr):
    def arr_gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    Result=arr[0]
    for num in arr[1:]:
        Result=arr_gcd(Result,num)
        if Result==1:
            return 1
    return Result

arr1 = [2,5,6,9,10]

print(find_arr(arr1))
