def palindrome(arr):
    new=str(arr)
    low=0
    high=len(new)-1
    while low<high:
        if new[low]!=new[high]:
            return False
        low+=1
        high-=1
    return True

arr=121
print(palindrome(arr))