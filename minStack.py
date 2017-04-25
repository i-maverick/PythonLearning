class MinStack:
    def __init__(self):
        self.__stack = []
        self.__min = []

    def min(self):
        return self.__min[-1] if self.__min else None

    def push(self, v):
        self.__stack.append(v)
        if not self.__min or v <= self.min():
            self.__min.append(v)
        return v

    def pop(self):
        if self.__stack:
            v = self.__stack.pop()
            if v == self.min():
                self.__min.pop()
            return v

s = MinStack()
print("push:", s.push(3))
print("push:", s.push(7))
print("push:", s.push(2))
print("push:", s.push(2))
print("push:", s.push(1))
print("push:", s.push(5))
print("push:", s.push(9))

print("pop:", s.pop())
print("min: ", s.min())
print("pop:", s.pop())
print("min: ", s.min())
print("pop:", s.pop())
print("min: ", s.min())
print("pop:", s.pop())
print("min: ", s.min())
print("pop:", s.pop())
print("min: ", s.min())
print("pop:", s.pop())
print("min: ", s.min())
print("pop:", s.pop())
print("min: ", s.min())
print("pop:", s.pop())
print("min: ", s.min())
