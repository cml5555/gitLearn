dict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
}
a = input().split()
a = list(map(int, a))


def out(s: int):
    if s in dict.keys():
        print(dict[s], end=' ')
    else:
        x = int(str(s)[0])
        x = x * 10
        y = int(str(s)[1])
        print(dict[x], end=' ')
        print(dict[y], end=' ')


out(a[0])
out(a[1])
