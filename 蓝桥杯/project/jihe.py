an=int(input())
a=input().split()
bn=int(input())
b=input().split()
def maopao(s):
    for i in range(len(s)):
        for j in range(len(s) - i - 1):
            if int(s[j]) > int(s[j + 1]):
                s[j], s[j + 1] = s[j + 1], s[j]
temp=[]
temp1=b
temp2=a
for i in range(an):
    if a[i] in b:

        temp.append(a[i])

    if a[i] not in b:
        temp1.append(a[i])
for i in range(len(temp)):
    temp2.remove(temp[i])

maopao(temp)
maopao(temp1)
maopao(temp2)
if len(temp)>0:
 for j in range(len(temp)):
     print(temp[j],end=' ')
 print(" ")
if len(temp1)>0:
 for i in range(len(temp1)):
     print(temp1[i], end=' ')
 print(" ")
if len(temp2)>0:
 for i in range(len(temp2)):
     print(temp2[i], end=' ')
