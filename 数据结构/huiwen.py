from typing import List


class Solution:
    def huiwen(self,x:int)->bool:
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
a=Solution()
print(Solution().huiwen(123))

