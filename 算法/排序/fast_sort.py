def patition(left, right, s):
    temp = s[left]

    while right > left:
        while right > left and s[right] >= temp:
            right = right - 1

        s[left] = s[right]

        while right > left and s[left] <= temp:
            left = left + 1

        s[right] = s[left]

    s[left] = temp
    return left


def fast_sort(left, right, s):
    if left < right:
        mid = patition(left, right, s)
        fast_sort(left, mid - 1, s)
        fast_sort(mid + 1, right, s)


a = [1, 2, 4, 2, 7, 3]
fast_sort(0, len(a) - 1, a)
print(a)
