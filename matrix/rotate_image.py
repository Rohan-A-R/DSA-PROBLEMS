def rotate_matrix(matrix):
    n=len(matrix)
    rotated=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i]=matrix[i][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j]=rotated[i][j]

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix(matrix))
    


# optimal

def optimal_matrix(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for row in matrix:
        row.reverse()
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(optimal_matrix(matrix))
   

# optimal for anti clock wise

def optimal_anti_clock(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    
    for j in range(n):
        low=0
        bot=n-1
        while low< bot:
            matrix[low][j],matrix[bot][j]=matrix[bot][j],matrix[low][j]
            low+=1
            bot-=1
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(optimal_anti_clock(matrix))