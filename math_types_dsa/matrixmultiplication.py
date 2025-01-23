
def matrix(a,b):
    m=len(a)
    n=len(a[0])
    p=len(b)
    q=len(b[0])


    if n !=p:
        raise ValueError("number of coloums of a and number rows of b should be equal")
    
    result=[[0 for _ in range(q)] for _ in range(m)]
    print(result)

    for i in range(m):
        for j in range(q):
            for k in range(n):
                result[i][j] +=a[i][k]*b[k][j]
    return result


A=[[1,2,3],
   [4,5,6],
   [7,8,9]]

B=[[4,2],
   [8,9],
   [5,3],]

result= matrix(A,B)
for row in result:
    print(row)  

