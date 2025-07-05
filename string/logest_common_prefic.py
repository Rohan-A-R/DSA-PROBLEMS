def lonhest_common_frefix(arr):
    res=str()
    for i in range(len(arr[0])):
        char=arr[0][i]
        for s in arr[1:]:
            print(s)
            if i >=len(s)  or  s[i]!=char:
                return res
        res+=char

    return res


arr=["geeksforgeeks", "geeks", "geek", "geezer"]

print(lonhest_common_frefix(arr))


