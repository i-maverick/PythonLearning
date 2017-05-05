def make_dict(keys, values):
    d = dict.fromkeys(keys)
    for i,v in enumerate(d):
        if i >= len(values):
            break
        d[i] = values[i]
    return d


keys = [0, 1, 2, 3, 4, 5]
values = ['zero', 'one', 'two', 'three']
print make_dict(keys, values)

from itertools import izip_longest
print {k: v for k, v in izip_longest(keys, values) if k is not None}
