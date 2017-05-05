ops = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y)
}


def shunting_yard(exp):
    res = []
    s = []

    def parse(exp):
        number = ''
        prev = ''
        sign = 1
        for s in exp:
            if s == '-' and (prev == '' or prev == '('):
                sign = -1
                continue
            prev = s

            if s in ".0123456789":
                number += s
            elif number:
                yield float(number) * sign
                sign = 1
                number = ''
            if s in ops or s in "()":
                yield s
        if number:
            yield float(number) * sign

    def pop_stack():
        while s:
            j = s.pop()
            if j == '(':
                return
            res.append(j)

    for i in parse(exp):
        if i in ops:
            if s and s[-1] in ops and ops[i][0] <= ops[s[-1]][0]:
                res.append(s.pop())
            s.append(i)
        elif i == '(':
            s.append(i)
        elif i == ')':
            pop_stack()
        else:
            res.append(i)

    pop_stack()
    return res


def calculate(exp):
    stack = []
    for i in shunting_yard(exp):
        if i in ops:
            y = stack.pop()
            x = stack.pop() if stack else 1
            stack.append(ops[i][1](x, y))
        else:
            stack.append(i)
    return stack[0]


exp = "-2 + ((-4.5*8+10)/4+1.25)-21"  # -28.25
print(calculate(exp))
