a=int()
s=input().split()
s= list(map(int,s))
for i in range(len(s)):
   for j in range(len(s)-i-1):
    if s[j]>s[j+1]:
        s[j],s[j+1]=s[j+1],s[j]
for i in range(len(s)):
    print(s[i],end=" ")