class Rectangle():
    def qiege(self,x:int,y:int)->int:
        sum=0
        while x!=1 and y!=1:
         if x==y:
            break
         if x>y:
            x=x-y
            sum=sum+1
         if x<y:
            y=y-x
            sum=sum+1
        return sum+1
print(Rectangle().qiege(2019,324))