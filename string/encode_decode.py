def encode(strs):
    encoded=""
    for s in strs:
        encoded+=f"{len(s)}:{s}"
    return encoded

def decode(encoded_str):
    decoded=[]
    i=0
    while i < len(encoded_str):
        j=encoded_str.find(":",i)
        length=int(encoded_str[i:j])
        decoded.append(encoded_str[j+1:j+1+length])
        i=j+1+length
    return decoded

str= ["Hello", "World"]
encodedd=encode(str)
print(encodedd)
print(decode(encodedd))






