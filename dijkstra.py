def dijkstra_algo(graph, start):
    weight = {start: 0}
    parents = {start: 0}
    for i in graph:
        for j in graph[i]:
            if i in weight:
                if j not in weight or graph[i][j] + weight[i] < weight[j]:
                    weight[j] = graph[i][j] + weight[i]
                    parents[j] = i
    return weight, parents

g_wiki = {
    1: {2: 7, 3: 9, 6: 14},
    2: {1: 7, 3: 10, 4: 15},
    3: {4: 11, 6: 2, 1: 9, 2: 10},
    4: {5: 6, 3: 11, 2: 15},
    5: {6: 9, 4: 6},
    6: {1: 14, 5: 9, 3: 2}
}

print dijkstra_algo(g_wiki, 1)
