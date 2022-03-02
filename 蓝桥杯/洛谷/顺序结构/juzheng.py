n=input().split()
n=list(map(int,n))
a=[]
sum=0
for i in range(n[0]):
 temp=input().split()
 a.append(list(map(int,temp)))
for i in range(n[0]):
  for j in range(n[1]):
    sum=sum+min(a[i][0],a[i][-1])*pow(2,j+1)
    if a[i][0]>a[i][-1]:
        del a[i][-1]
    else:
        del a[i][0]
  print(sum,i)
print(sum)