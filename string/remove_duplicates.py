def removeDups(str1):
	arr=set()
	res=""
	for num in str1:
		if num not in arr:
		    arr.add(num)
		    res+=num
	return res


new="roohan"
print(removeDups(new))

