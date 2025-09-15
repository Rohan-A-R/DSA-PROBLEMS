def bruteforce(arr,k):
    vol=['a','e','i','o','u']
    max_elmen=0
    for i in range(len(arr)-k+1):
        current=0
        for j in range(i,k+i):
            if  arr[j] in vol:
                current+=1
        max_elmen=max(current,max_elmen)
    return max_elmen


s = "abciiidef"
k = 3
print(bruteforce(s,k))

def maxVowels(arr,k):
        vol=['a','e','i','o','u']
        max_elment=0
        current=0
        for i in range(len(arr)):
            if arr[i] in vol:
                current+=1

            if i>=k and arr[i-k] in vol:
                current-=1
            max_elment=max(current,max_elment)

            if max_elment==k:
                return k
        return max_elment


s = "abciiidef"
k = 3
print(maxVowels(s,k))