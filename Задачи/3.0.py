import random

lines = open("lines.txt", "rt", encoding="utf8").read().splitlines()
if len(lines) != 0:
    print(random.choice(lines))
