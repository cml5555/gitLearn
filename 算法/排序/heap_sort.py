def sift(s, low, high):
    i = low
    j = 2 * i + 1
    temp = s[i]
    while j <= high:
        if s[j] < s[j + 1] and j < high:
            j = j + 1
        if temp < s[j]:
            s[i] = s[j]
            i = j
            j = 2 * i + 1
        else:
            break
    s[i] = temp


def heap_sort(s):
    n = len(s)
    for i in range((n - 2) // 2, -1, -1):
        sift(s, i, n - 1)
    for i in range(n - 1, -1, -1):
        s[0], s[i] = s[i], s[0]
        sift(s, 0, i - 1)


a = [2, 1, 4, 5]
heap_sort(a)
print(a)
