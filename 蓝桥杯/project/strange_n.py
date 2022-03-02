class Solution:
    def sum(self,n:int)->int:
        sum=0
        key_list=['0','1','2','9']
        for i in range(n+1):
          if  any(key in str(i) for key in key_list):
              sum=sum+i

        return sum
print(Solution().sum(40))
