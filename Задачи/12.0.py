def chek(x_01, x_11, x_02, x_12):
    return x_02 <= x_01 <= x_12 or x_01 <= x_02 <= x_11


x0, y0, r0 = [int(i) for i in input().split()]
x1, y1, r1 = [int(i) for i in input().split()]
d = (x0 - x1) ** 2 + (y0 + y1) ** 2
r = (r0 + r1) ** 2
if r >= d or d > abs(r0 - r1) ** 2:
    print("YES")
else:
    print("NO")
