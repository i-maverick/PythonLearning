planets = [
    'Earth',
    'Mars',
    'Venus',
    'Mercury',
    'Jupiter',
    'Saturn',
    'Neptune',
    'Uranus',
    'Pluto'
]

routes = [
    (0, 3),
    (0, 8),
    (1, 4),
    (1, 7),
    (2, 3),
    (2, 8),
    (3, 8),
    (4, 5),
    (5, 6),
    (6, 7)
]

graph = [
    [3, 8],
    [4, 7],
    [3, 8],
    [8],
    [5],
    [6],
    [7]
]

g = {
    1: [2, 3],
    2: [4]
}


def find_path(graph, start, end):
    open = [start]
    close = []
    v = open.pop(0)
    close.append(v)
    for i in graph[v]:
        open.append(i)


print(find_path(g, 1, 4))


def method4():
    return ''.join([repr(num) for num in range(100)])


print(method4())
