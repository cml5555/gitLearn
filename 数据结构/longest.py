class Solution():
    def longest(self,x:[]):
        sum=0

        for j in range(min(len(x[0]),len(x[1]))):

             if x[0][j]==x[1][j]:
                sum=sum+1
        return sum
x=["cchhen","chcc"]
l=Solution().longest(x)
print(x[0][:l])