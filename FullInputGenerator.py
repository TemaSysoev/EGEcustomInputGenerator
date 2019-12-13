import math, random

niceLine = """
=============
"""
print("Кастомизировать? (0 - нет, any - да)")
custom = int(input())
length = 0
number = 0
divider = 1
minRange = 0
maxRange = 100
sort = 0

if custom == 0:
    number = 5
    for _ in range(0, number):
        length = random.randrange(4, 10, 1)
        print(niceLine)
        print(length)
        for _ in range(0, length):
            a = random.randrange(0, 100, 1)
            print(a)
    print(niceLine)
else:
    print("Количество наборов:")
    number = int(input())
    print("Длина:")
    length = int(input())
    print("Минимальное значение:")
    minRange = int(input())
    print("Максимальное значение:")
    maxRange = int(input()) + 1
    print("Делитель")
    divider = int(input())
    print("Сортировка (0 - нет, 1 - min_max, 2 - max_min)")
    sort = int(input())
    print(niceLine)
    for _ in range(0, number):
        print(length)
        result = []
        for _ in range(0, length):
            a = random.randrange(minRange, maxRange, 1)
            a = (a // divider) * divider
            for item in result:
                if a == item:
                    for _ in range(0, 10):
                        a = random.randrange(minRange, maxRange, 1)
                        a = (a // divider) * divider
                        if a != item:
                            continue
            result.append(a)
        if sort == 1:
            result.sort()
        if sort == 2:
            result.sort(reverse=True)

        for index in result:
            print(index)
        print(niceLine)
