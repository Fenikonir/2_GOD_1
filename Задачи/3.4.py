with open("prices.txt", "rt", encoding="utf-8") as f:
    f1 = f.read().split("\n")
    print(f1)
if bool(f1):
    s = 0
    for i in range(len(f1)):
        x = f1[i].split("\t")
        s += float(x[1]) * float(x[2])
    print(s)
else:
    print(0)
