import time
import banners


class simpleStack:
    def __init__(self, st=[]):
        self.__stack = st

    def push(self, obj):
        self.__stack.append(obj)

    def pop(self):
        return self.__stack.pop()

    def top(self):
        if (not self.empty()):
            return self.__stack[-1]

    def empty(self):
        return False if self.__stack else True

    def __str__(self):
        return str(self.__stack)


def sortStack(s):
    mid = s.top()
    print("mid:", mid)

    left = simpleStack([])
    right = simpleStack([])
    leftCount = 0
    rightCount = 0
    while not s.empty():
        i = s.pop()
        if i < mid:
            left.push(i)
            leftCount += 1
        else:
            right.push(i)
            rightCount += 1
    if leftCount == 1:
        s.push(left.pop())
    elif leftCount > 1:
        sortStack(left)
    if rightCount == 1:
        s.push(right.pop())
    elif rightCount > 1:
        sortStack(right)


s = simpleStack()
st = list(range(-3, 5))
for i in banners.randomNums(st):
    s.push(i)
print(s)
sortStack(s)
# t = time.time()
# while not s.empty():
#     a = s.pop()
# print("Time:", time.time() - t)
