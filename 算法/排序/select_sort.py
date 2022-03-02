def select_sort(s):
    for i in range(len(s)-1):
        min_loc=i
        for j in range(i+1,len(s)):
            if (s[j]<s[min_loc]):
                min_loc=j
        s[i],s[min_loc]=s[min_loc],s[i]
a=[1,3,2,5,7]
select_sort(a)
print(a)