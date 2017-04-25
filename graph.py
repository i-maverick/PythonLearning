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


# def width_search(start, end, path=None):
#     if not path:
#         path = []
#     path.append(start)
#     while end not in path:
#         for i in graph[start]:
#             if i not in path:
#                 width_search(i, end, path)

# print find_path(1, 8)
# for path in find_all_paths(1, 8):
#     print path
# print find_shortest_path(1, 8)
#print width_search(1, 8)

adj = [
    [1, 3],         #0
    [0, 3, 4, 5],   #1
    [4, 5],         #2
    [0, 1, 5],      #3
    [1, 2],         #4
    [1, 2, 3]       #5
]
visited = set()

def dfs(v):
    visited.add(v)
    for vertex in adj[v]:
        if vertex not in visited:
            dfs(vertex)

level = [-1] * len(adj)

def bfs(s):
    level[s] = 0
    stack = [s]
    while stack:
        v = stack.pop(0)
        for w in adj[v]:
            if level[w] is -1:
                stack.append(w)
                level[w] = level[v] + 1

bfs(0)
print(level[1])
