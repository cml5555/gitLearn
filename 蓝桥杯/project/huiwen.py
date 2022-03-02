n = input().split()
n = list(map(int, n))
a = []
s = []
for i in range(n[0]):
    temp = input().split()
    temp = list(map(int, temp))
    a.append(temp)
i = 0
j = 0
print(a)
count = 0
flag_j = 1
flag_i = 0
if len(a) == 1:
    for i1 in range(len(a[0])):
        print(a[0][i1], end=' ')

if len(a) > 1:
    for p in range(n[0] * n[1]):
        s.append(a[j][i])
        print(s)
        print(len(s))
        print("i,j", i, j)
        if j == n[0] - 1 and i == 0:
            flag_i = 1
            flag_j = 0
        if j == n[0] - 1 and i == n[1] - 1:
            flag_i = 0
            flag_j = -1
        if j == 0 and i == n[1] - 1:
            flag_j = 0
            flag_i = -1
        if j == 0 and i == 1:
            flag_i = 0
            flag_j = 1
        j = j + flag_j
        i = i + flag_i

