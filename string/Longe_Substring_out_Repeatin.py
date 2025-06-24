def longest_Substring(s):
    start=0
    max_length=0
    char_set=set()
    for nums in range(len(s)):
        while s[nums] in char_set:
            char_set.remove(s[start])
            start+=1
        char_set.add(s[nums])
        max_length=max(max_length,nums-start+1)
    return max_length

s1 = "geeksforgeeksabcdefghjkl"
print(longest_Substring(s1))



# How would you modify the function to return the substring itself instead of just its length?

def longest_unique_substring_with_result(s):
    start = 0
    max_length = 0
    char_set = set()
    result = ""

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        if max_length < end - start + 1:
            max_length = end - start + 1
            result = s[start:end + 1]

    return result


s = "geeksforgeeks"
print(longest_unique_substring_with_result(s))  


# bruteforce
def brute_force(s):
    max_sum=0
    for i in range(len(s)):
        arr=set()
        for j in range(i,len(s)):
            if s[j] in arr:
                break
            arr.add(s[j])
            max_sum=max(max_sum,j-i+1)

    return max_sum

s = "geeksforgeeksabcdefghjkl"
print(brute_force(s))

