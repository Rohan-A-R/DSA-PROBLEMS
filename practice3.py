# def frequent(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     return freq



# arr=[1,1,2,1,3,2,1]

# print(frequent(arr))




def palindrome(string):
    string1=[]
    for num in string:
        string1.append(num)
    

    
    for num1 in string:
        if num1!=string1.pop():
            return False
    return True



print(palindrome("oho"))

    