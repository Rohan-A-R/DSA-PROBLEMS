def merge_2sorted_array(a,b):
    m=len(a)
    n=len(b)
    a.extend([0]*n)
    last=m+n-1
    while m >0 and n>0:
        if a[m-1]>b[n-1]:
            a[last]=a[m-1]
            m-=1
        else:
            a[last]=b[n-1]
            n-=1
        last-=1
    while n>0:
        a[last]=b[n-1]
        n-=1
        last-=1

    return a
a = [1]
b= []
print(merge_2sorted_array(a,b))


def mergeArrays(self, a, b):
        i=len(a)-1
        j=0
        while i>=0 and j<len(b):
            if a[i]>b[j]:
                a[i],b[j]=b[j],a[i]
                i-=1
                j+=1
            else:
                break
        a.sort()
        b.sort()