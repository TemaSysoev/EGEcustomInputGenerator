import math, random

niceLine = """
=============
"""

number = 5
print(niceLine)
for _ in range(0, number):
    length = random.randrange(4, 10, 1)

    print(length)
    for _ in range(0, length):
        a = random.randrange(0, 100, 1)
        print(a)
    print(niceLine)
