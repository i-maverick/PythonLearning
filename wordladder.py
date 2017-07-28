from collections import defaultdict
from itertools import permutations


def build_graph(wordfile):
    d = defaultdict(list)
    g = defaultdict(list)
    with open(wordfile, 'r') as f:
        for line in f:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                d[bucket].append(word)

    for bucket in d:
        for word1, word2 in permutations(d[bucket], 2):
            g[word1].append(word2)

    return g


def bfs(graph, start):
    queue = [start]
    visited = set()
    depths = dict()
    parents = {}
    depths[start] = 0

    while queue:
        current = queue.pop(0)
        visited.add(current)
        for v in graph[current]:
            if v not in visited:
                queue.append(v)
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


g = build_graph('wordladder.txt')
d, p = bfs(g, 'fool')
path(d, p, 'sage')
