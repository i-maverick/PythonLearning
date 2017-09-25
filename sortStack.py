import banners


class SimpleStack:
    def __init__(self):
        self.items = []

    def push(self, obj):
        self.items.append(obj)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return self.items == []

    def __str__(self):
        return str(self.items)


def sort_stack(s):
    mid = s.peek()
    print("mid:", mid)

    left = SimpleStack()
    right = SimpleStack()
    left_count = 0
    right_count = 0
    while not s.empty():
        i = s.pop()
        if i < mid:
            left.push(i)
            left_count += 1
        else:
            right.push(i)
            right_count += 1
    if left_count == 1:
        s.push(left.pop())
    elif left_count > 1:
        sort_stack(left)
    if right_count == 1:
        s.push(right.pop())
    elif right_count > 1:
        sort_stack(right)


s = SimpleStack()
st = list(range(-3, 5))
for i in banners.random_nums(st):
    s.push(i)
print(s)
sort_stack(s)
print(s)
# t = time.time()
# while not s.empty():
#     a = s.pop()
# print("Time:", time.time() - t)
