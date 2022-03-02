class Solution:
   symbol_values={
       'I':1,
       'V':5,
       'X':10,
       'L':50,
       'C':100,
       'D':500,
       'M':1000
   }
   def roman(self,s:str)->int:
       ans=0
       n=len(s)
       i=1
       for i in range(n):
           if Solution().symbol_values[s[i]]>=Solution().symbol_values[s[i-1]]:
               ans=Solution().symbol_values[s[i-1]]+ans
           else:
               ans=Solution().symbol_values[s[i]]-ans
       return ans
a=Solution()
print(a.roman('IIVV'))