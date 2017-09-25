from itertools import zip_longest

keys = [0, 1, 2, 3, 4, 5]
values = ['zero', 'one', 'two', 'three']

d = dict.fromkeys(keys)
for k, v in zip(keys, values):
    d[k] = v
print(d)

d = {k: v for k, v in zip_longest(keys, values) if k is not None}
print(d)

from itertools import groupby

city_list = [
    ('Decatur', 'AL'),
    ('Huntsville', 'AL'),
    ('Selma', 'AL'),
    ('Anchorage', 'AK'),
    ('Nome', 'AK'),
    ('Flagstaff', 'AZ'),
    ('Phoenix', 'AZ'),
    ('Tucson', 'AZ')
]


def get_state(tpl):
    return tpl[1]

# city_list.sort(key = lambda x: x[1])
for k,v in groupby(city_list, get_state):
    print(k, [x[0] for x in v])

lst = [-1, -2, -1, 10, 10, 10, -1, -1, -1, 10, -1, 10]


def group_ints(lst, key=0):
    return [list(g) for _, g in groupby(lst, lambda x: x < key)]

print(group_ints(lst, 5))

for _, g in groupby(sorted(lst), lambda x: x < 0):
    print(list(g))
