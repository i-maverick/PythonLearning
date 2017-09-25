import re

numbers = ['+79265677789', '89265677789', '+7(926)567778a', '8(926) 567-7789', '+7 (926) 567-77-89', '+7(926) 567 77 89',
           '+89264622576']
for n in numbers:
    s = re.sub(r'[()\s-]', '', n)
    if s[0] == '+':
        if len(s) != 12:
            print('{} - Error'.format(n))
            continue
    else:
        if len(s) != 11:
            print('{} - Error'.format(n))
            continue
    res = re.match(r'^(\+7|8)\d+$', s)
    if res:
        print('{} - Success'.format(n))
    else:
        print('{} - Error'.format(n))
    n = s

print(numbers)

print(re.findall(r'^\w+$', 'hello_123'))
