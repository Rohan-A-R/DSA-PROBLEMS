def vowles_reverse(s):
    arr=list(s)

    vowles=["a","e","i","o","u"]
    low=0
    high=len(arr)-1
    while low<high:
        if arr[low].lower() in vowles and arr[high].lower() in vowles:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
        elif arr[low].lower() in vowles and arr[high].lower() not in vowles:
            high-=1
        elif arr[low].lower() not in vowles and arr[high].lower()  in vowles:
            low+=1

        else:
            low+=1
            high-=1
    return "".join(arr)

s = "IceCreAm"
print(vowles_reverse(s))



