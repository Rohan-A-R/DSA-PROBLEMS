class Solution:
    def reverseWords(s):
      string=s.split()
      result=string[::-1]
      return ' '.join(result)
    
new=Solution.reverseWords
    
print(new('rohan is a good boy and bad'))

