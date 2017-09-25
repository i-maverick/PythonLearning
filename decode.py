def decode(exp):
    res = []
    s = str(exp).split('98')
    if '' in s:
        s.remove('')
    for i in range(len(s)):
        if i % 2 == 0:
            to_char = lambda x: chr(int(s[i][x:x+3]) - 4)
            res.append(''.join([to_char(x) for x in range(0, len(s[i]), 3)]))
        else:
            res.append(str(int(s[i], 2)))
    return ', '.join(res)

assert(decode(103115104105123101118119981001098) == 'codewars, 18')
assert(decode(103115104105123101118119981001098113113113981000) == "codewars, 18, mmm, 8")
