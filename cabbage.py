# peasant, wolf, goatat, cabbage
graph = {
    'peasant-wolf-goat-cabbage / ': ['wolf-cabbage / peasant-goat'],
    'wolf-cabbage / peasant-goat': ['peasant-wolf-cabbage / goat'],
    'peasant-wolf-cabbage / goat': ['cabbage / peasant-wolf-goat', 'wolf / peasant-goat-cabbage'],
    'cabbage / peasant-wolf-goat': ['peasant-goat-cabbage / wolf'],
    'peasant-goat-cabbage / wolf': ['goat / peasant-wolf-cabbage'],
    'wolf / peasant-goat-cabbage': ['peasant-wolf-cabbage / goat', 'peasant-wolf-goat / cabbage'],
    'peasant-wolf-goat / cabbage': ['wolf / peasant-goat-cabbage', 'goat / peasant-wolf-cabbage'],
    'goat / peasant-wolf-cabbage': ['peasant-goat / wolf-cabbage'],
    'peasant-goat / wolf-cabbage': [' / peasant-wolf-goat-cabbage'],
    ' / peasant-wolf-goat-cabbage': ['peasant-goat / wolf-cabbage']
}


def bfs(g, start):
    stack = [start]
    visited = set()
    depths = dict()
    parents = dict()
    depths[start] = 0

    while stack:
        current = stack.pop(0)
        visited.add(current)
        for v in g[current]:
            if v not in visited:
                stack.append(v)
                depth = depths[current] + 1
                if v not in depths or depth < depths[v]:
                    depths[v] = depth
                    parents[v] = current

    return depths, parents


def path(depths, parents, v):
    print(depths[v])
    while v:
        print(v)
        v = p[v] if v in p else None


d, p = bfs(graph, 'peasant-wolf-goat-cabbage / ')
path(d, p, ' / peasant-wolf-goat-cabbage')
