import math, random

niceLine = """
=============
"""

number = 5
print(niceLine)
for _ in range(0, number):
    length = random.randint(4, 10)

    print(length)
    for _ in range(0, length):
        a = random.randint(0, 100)
        print(a)
    print(niceLine)
