def flowers_bed(arr,n):
    flowers=[0]+arr+[0]
    for i in range(1,len(flowers)-1):
        if flowers[i-1]==0 and flowers[i]==0 and flowers[i+1]==0:
            flowers[i]=1
            n-=1
    return n<=0


arr=[1,0,0,0,1]
n=1
print(flowers_bed(arr,n))