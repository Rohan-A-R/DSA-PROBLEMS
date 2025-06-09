class Solution:
    def reverseWords(s):
      string=s.split()
      print(string)
      result=string[::-1]
      return ' '.join(result)
    
new=Solution.reverseWords
    
print(new('rohan is a good boy     and bad'))


def reverse_word(s):
  string=s.split()
  result=[]
  for i in range(len(string)-1,-1,-1):
    result.append(string[i])
  return " ".join(result)


print(reverse_word("rohan ar"))

