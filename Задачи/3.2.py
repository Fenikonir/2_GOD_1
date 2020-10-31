

def reverse():
    with open("input.dat", "rb", encoding="utf-8") as f:
        f1 = "".join(f.read().split().reverse())
    with open('output.dat', "wb", encoding="utf-8") as f:
        f.write(f1)
