with open("candies.txt", "rt", encoding="utf-8") as f:
    perv, flor = f.read().split("\n")[:2]
v1 = perv.split()
v2 = list(flor.lower())
b = []
for i in v1:
    for j in v2:
        if j in i.lower():
            if i not in b:
                b.append(i)
            continue
for i in range(len(b)):
    b[i] = b[i].capitalize()
a = ", ".join(b)
with open("secret.txt", "wt", encoding="utf-8") as f1:
    if len(b) != 0:
        f1.write(a)
    else:
        f1.write(None)

