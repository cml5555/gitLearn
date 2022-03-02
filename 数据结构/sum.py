from typing import List
import numpy
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        n=len(nums)
        a = numpy.zeros((2,2))
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                  a[count]=[i,j]
                  count=count+1
        return a
nums=[1,2,7,8]
target=9
a=Solution()
obj=a.twoSum(nums,target)
print(obj)