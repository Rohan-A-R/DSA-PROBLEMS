

def insert_element(arr,index,element):
    for i in range(index,len(arr)):
        arr[i],element=element,arr[i]
    arr.append(element)


arr=[1,2,3,5,6,7]
index=3
element=4

insert_element(arr,index,element)
print(arr)