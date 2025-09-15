def spiral_matrix(arr):
    top=0
    right=len(arr[0])-1
    left=0
    bottom=len(arr)-1
    result=[]
    
    while top<=bottom and left<=right:
        for  row in range(left,right+1):
            result.append(arr[top][row])
        top+=1
        
        for col in range(top,bottom+1):
            result.append(arr[col][right])
        right-=1
        
        if top<=bottom:
        
            for bot in range(right,left-1,-1):
                result.append(arr[bottom][bot])
            bottom-=1
        if left<=right:
        
            for col  in range(bottom,top-1,-1):
                result.append(arr[col][left])
            left+=1
    return result
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))

    
    
    
    