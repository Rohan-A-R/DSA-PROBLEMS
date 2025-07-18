def string_comression(chars):
    low=0
    high=0
    while high<len(chars):
        count=0
        current_char=chars[high]
        while high<len(chars) and current_char==chars[high]:
            high+=1
            count+=1
        chars[low]=current_char
        low+=1
        if count>1:
            for num in str(count):
                chars[low]=num
                low+=1

    return low

chars = ["a","a","b","b","c","c","c"]
print(string_comression(chars))