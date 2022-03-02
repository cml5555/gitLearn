def insert_sort(s):
    for i in range(len(s)-1):
        temp=s[i+1]
        j=i
        while temp<s[j] and j>=0:
            s[j+1]=s[j]
            j=j-1
        s[j+1]=temp
a=[1,3,2,5,4]
insert_sort(a)
print(a)