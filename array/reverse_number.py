# reverse number without leading zero
def reverse_number(n):
    s=str(n)
    s=list(s)   
    s.reverse()
    s="".join(s)
    n=int(s)
    return n


print(reverse_number(4560))



# Reverse Integer Letcode

def reverse_integer(n):
    min_int,max_int= -2**31, 2**31 - 1
    if n<0:
        sign=-1
    else:
        sign=1
    n=abs(n)
    reversed_str=str(n)[::-1]
    reversed_int=int(reversed_str)*sign
    if reversed_int < min_int  or reversed_int>max_int:
        return 0
    return reversed_int

print(reverse_integer(-4555))

    
