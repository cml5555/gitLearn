class Solution:
    def reverse(self,x:int)->int:
        rev=0
        min=-2**31
        max=2**31-1
        while x!=0:
           if rev<min//10+1 or rev>max//10:
               return 0
           digit=x%10
           if x<0 and digit>0:
               digit=digit-10
           x=(x-digit)//10

           rev=rev*10+digit

        return rev
a=Solution()
print(a.reverse(-1234))
