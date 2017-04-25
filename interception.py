import time


def findInterception(a, b):
    x, y = -1, -1
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i] == b[k]:
                if x >= 0 and y >= 0 and i == x + 1 and k == y + 1:
                    print(a[x] + a[i])
                    return x, y
                x, y = i, k
    return None


a = "adskfha;dlkfja;ldskjg,mfvnsdkhfoqiejrlkqewm,nm"
b = "powirptoj.f,gmb,xmnclvksdjf[osierjgfd[rpgk;ldmf"
t = time.time()
print(findInterception(a, b))
print("time:", time.time() - t)
