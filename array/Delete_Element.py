def delet_element(arr,element):
    if element not in arr:
        return "enter the currect element"
    
    result=[]

    for i in range(len(arr)):
        if arr[i] != element:
            result.append(arr[i])
    return result


arr=[1,2,3,4,5,6]

element=3

print(delet_element(arr,element))