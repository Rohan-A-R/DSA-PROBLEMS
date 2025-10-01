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
a = [1,3,5,6,10]
b= [2,4,7,8]
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
        
        
def merege(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    last=m+n-1
    i=j=0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            arr1[last]=arr1[i]
            i+=1
        else:
            arr2[last]=arr2[j]
            j+=1
        last+=1
        