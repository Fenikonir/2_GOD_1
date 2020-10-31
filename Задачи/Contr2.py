import math


a = input()
b = input()
with open(a, "rt", encoding="utf-8") as f:
    chet, maks = f.read().split("\n")
with open(b, "rt", encoding="utf-8") as f1:
    a = f1.read().split("\n")
d = []
chet = int(chet)
maks = float(maks)
for i in range(len(a)):
    c = a[i].split()
    print(a)
    print(c)
    c1 = c[0]
    c2 = c[1]
    if chet == 1:
        if c1 > 0 and c2 > 0:
            if math.sqrt(c1**2 + c2**2) <= maks:
                d.append(c1, c2)
    elif chet == 2:
        if c1 < 0 and c2 > 0:
            if math.sqrt(c1**2 + c2**2) <= maks:
                d.append(c1, c2)
    elif chet == 3:
        if c1 < 0 and c2 < 0:
            if math.sqrt(c1**2 + c2**2) <= maks:
                d.append(c1, c2)
    else:
        if math.sqrt(c1 ** 2 + c2 ** 2) <= maks:
            d.append(tuple(c1, c2))
with open("lucky.txt", "wt", encoding="utf-8") as f:
    for i in d:
        f.write(i)

