x = int(input())
min = x // 10000 % 10
x1 = x // 1000 % 10
x2 = x // 100 % 10
x3 = x // 10 % 10
x4 = x % 10
if min > x1:
    min = x1
if min > x2:
    min = x2
if min > x3:
    min = x3
if min > x4:
    min = x4
print(min)
