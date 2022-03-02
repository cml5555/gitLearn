import sys
n=input()
if int(n)<=0 or int(n)>10:
    sys.exit()
aa=[]
sum_a=0
for i in  range(int(n)):
          aa.append(str(input()))

dic={
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15,
}
for j in range(int(n)):
  sum_a=0
  for i in range(len(aa[j])):
      sum_a=sum_a+dic[aa[j][len(aa[j])-i-1]]*16**i
  a,y=divmod(sum_a,8)
  sum_a=a
  s=str(y)
  while a>0:
      a,y=divmod(sum_a,8)
      sum_a=a
      s=s+str(y)
  print(s[::-1])



