def check_brackets(s):
    st = []
    for i, c in enumerate(s):
        if c == '(':
            st.append(c)
        elif c == ')':
            if len(st) == 0 or st.pop() != '(':
                return s, i
    l = len(st)
    if l > 0:
        return s, l - 1
    return s, True

print(check_brackets('(())'))
print(check_brackets('((()'))
print(check_brackets('((asd)))'))
print(check_brackets(')('))
print(check_brackets(')'))
print(check_brackets('('))
print(check_brackets('()'))
print(check_brackets(''))
