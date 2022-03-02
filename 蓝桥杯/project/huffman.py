def paixu(s):
    for i in range(len(s)):
        for j in range(len(s)-i-1):
            if int(s[j])>int(s[j+1]):
                s[j],s[j+1]=s[j+1],s[j]
n=int(input())
a=input().split()
a=list(map(int,a))
paixu(a)
sum=0

for i in range(n-1):
    temp=int(a[0])+int(a[1])

    sum=sum+int(temp)

    del a[0]
    del a[0]
    a.append(temp)
    paixu(a)

print(sum)