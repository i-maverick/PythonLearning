import random


def rand2():
    return random.randint(0, 1)


def rand3():
    x, y = 1, 0
    while x == 1 and y == 0:
        x = rand2()
        y = rand2()
    return x + y


count0 = 0
count1 = 0
count2 = 0
n = 1000
for i in range(n):
    k = rand3()
    if k == 0:
        count0 += 1
    elif k == 1:
        count1 += 1
    elif k == 2:
        count2 += 1
print ("0 - ", count0 / n * 100, "%")
print ("1 - ", count1 / n * 100, "%")
print ("2 - ", count2 / n * 100, "%")
