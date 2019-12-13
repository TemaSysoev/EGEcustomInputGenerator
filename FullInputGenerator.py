import math
import random

niceLine = """
=============
"""
custom = int(input())
length = 0
number = 0
divider = 1
minRange = 0
maxRange = 100

if custom == 0:
    number = 5
    for _ in range(0, number):
        length = random.randrange(4, 10, 1)
        print(niceLine)
        print(length)
        for _ in range(0, length):
            a = random.randrange(0,100,1)
            print(a)
    print(niceLine)
else:
    number = int(input())
    length = int(input())
    minRange = int(input())
    maxRange = int(input())
    divider = int(input())