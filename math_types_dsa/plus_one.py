# 
def plus_one(arr):
    new=""
    for i in arr:
        new+=str(i)
    num=int(new)+1
    result=[]
    for i in str(num):
        result.append(int(i))

    return result





arr=[1,2,3]
print(plus_one(arr))

'''so here first list into string and then add 1 and this do for loop to str num and append to
    to result'''

