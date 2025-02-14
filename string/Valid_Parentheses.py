def Valid_paranthisi(s):
    hash_map={
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack=[]

    for char in s:
        if char in hash_map.values():
            stack.append(char)
        elif char in hash_map:
            if not stack or stack[-1]!=hash_map[char]:
                return False
            print(hash_map[char])
            stack.pop()

        else:
            return False
        
    return not stack

s = "[{()}]"
print(Valid_paranthisi(s)) 




