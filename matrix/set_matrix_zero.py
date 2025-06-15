def set_matrix_zero(matrix):
    row=len(matrix)
    col=len(matrix[0])
    marker=-1
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:

                for k in range(col):        #for rows to make zero
                    if matrix[i][k]!=0:
                        matrix[i][k]=marker
                
                for k in range(row):         #for col to make zero
                    if matrix[k][j]!=0:
                        matrix[k][j]=marker

    for i in range(row):
        for j in range(col):
            if matrix[i][j]==marker:
                matrix[i][j]=0
    return matrix





matrix=[[1,1,1],[1,0,1],[1,1,1]]

print(set_matrix_zero(matrix))