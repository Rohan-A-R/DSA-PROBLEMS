def substring_search(str,search):
    n=len(str)
    m=len(search)
    for i in range(n-m+1):
        if str[i:i+m]==search:
            return i
    return -1

str="GeeksForGeeks"
search="For"

print(substring_search(str,search))
