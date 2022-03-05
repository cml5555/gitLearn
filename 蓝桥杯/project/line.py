l=[[i,j]for i in range(20) for j in range(21)]
s=set()
ans=20
for i in range(len(l)-1):
    x1,y1=l[i][0],l[i][1]
    for j in range(i+1,len(l)):
        x2, y2 = l[j][0], l[j][1]
        if x1==x2:
            continue
        k=(y2-y1)/(x2-x1)
        b=(x1*y2-x2*y1)/(x1-x2)
        if (k,b) not in s:
            s.add((k,b))
            ans+=1
print(ans)
