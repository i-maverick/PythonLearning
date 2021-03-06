graph = {
    1: [2, 4, 5],
    2: [1, 6, 7],
    3: [4, 5, 8],
    4: [1, 3, 5],
    5: [1, 3, 4, 9],
    6: [2, 10],
    7: [2, 10, 11],
    8: [3, 11, 12],
    9: [5, 12],
    10: [6, 7, 11, 12],
    11: [7, 8, 10, 12],
    12: [8, 9, 10, 11]
}


def find_path(start, end, path=None):
    if not path:
        path = []
    path = path + [start]
    if end in path:
        return path
    if start not in graph:
        return None
    for i in graph[start]:
        if i not in path:
            new_path = find_path(i, end, path)
            if new_path:
                return new_path


def find_all_paths(start, end, path=None):
    if not path:
        path = []
    path = path + [start]
    if end in path:
        return [path]
    if start not in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(start, end, path=None):
    if not path:
        path = []
    path = path + [start]
    if end in path:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


adj = [
    [1, 3],         #0
    [0, 3, 4, 5],   #1
    [4, 5],         #2
    [0, 1, 5],      #3
    [1, 2],         #4
    [1, 2, 3]       #5
]


def dfs(v, visited = None):
    if not visited:
        visited = set()
    visited.add(v)
    print('visit {}'.format(v))
    for vertex in adj[v]:
        if vertex not in visited:
            dfs(vertex, visited)


def bfs(s):
    visited = {s: 0}
    stack = [s]
    while stack:
        v = stack.pop(0)
        for w in adj[v]:
            if w not in visited:
                stack.append(w)
                visited[w] = visited[v] + 1
    return visited


dfs(0)
levels = bfs(0)
print(levels[1])
