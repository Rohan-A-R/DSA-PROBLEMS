def diff_arr(arr1,arr2):
    answer1=[]
    for num in arr1:
        if num not in arr2 and num not in answer1:
            answer1.append(num)
    answer2=[]
    for num in arr2:
        if num not in arr1 and num not in answer2:
            answer2.append(num)
    return [answer1,answer2]

arr1=[1,2,3,3]
arr2=[1,1,2,2]


print(diff_arr(arr1,arr2))


def diff_arr1(arr1,arr2):
    set1=set(arr1)
    set2=set(arr2)
    arr3=list(set1-set2)
    arr4=list(set2-set1)
    return [arr3,arr4]

arr1=[1,2,3,3]
arr2=[1,1,2,2]


print(diff_arr1(arr1,arr2))