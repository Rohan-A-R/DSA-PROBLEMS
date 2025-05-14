def bad_version(n):
    left=1
    right=n
    while left < right:
        mid=(left+right)//2
        if isbadversion(mid):
            right=mid
        else:
            left=mid+1
        
    return left


def  isbadversion(mid):
    version=4
    if mid==version:
        return version
