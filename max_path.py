import math


def top_sort(adj_nodes):
    index = []
    number = 0
    deg_in = [0]*len(adj_nodes)
    for adj in adj_nodes:
        for v in adj_nodes[adj]:
            deg_in[v] = deg_in[v] + 1
    stack = []
    for v in adj_nodes:
        if deg_in[v] == 0:
            stack.append(v)

    while len(stack) != 0:
        v = stack.pop(-1)
        index.append(v)
        number += 1
        for w in adj_nodes[v]:
            deg_in[w] = deg_in[w] - 1
            if deg_in[w] == 0:
                stack.append(w)
    # print(index)
    return index


def find_max_path(graph, sorted_list, start, adj_nodes):
    distances = [-math.inf] * len(graph)
    distances[start] = 0
    previous = {start: -1}
    # print(graph)
    for k in range(0, len(graph)):
        vk = sorted_list[k]
        for w in adj_nodes[vk]:
            new_distance = distances[vk] + graph[vk][w]
            if new_distance > distances[w]:
                distances[w] = new_distance
                previous[w] = vk
    return (previous, distances)


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[-math.inf]*n for x in range(n)]
    adj_nodes = {x:[] for x in range(n)}
    # print(graph)
    for x in range(m):
        connected = [-math.inf]*n
        v, w, c = map(int, input().split())
        graph[v-1][w-1] = c
        adj_nodes[v-1].append(w-1)
    start, target = map(int, input().split())
    start = start - 1
    target = target - 1
    # adj_nodes = {5:[4,2,0], 0:[1,3], 2:[0], 1:[3]}
    # print(graph, 'graph ', n, m)
    # print(adj_nodes)
    sorted_list = top_sort(adj_nodes)
    # print(sorted_list)
    previous, distances = find_max_path(graph, sorted_list, start, adj_nodes)
    # print(previous, distances)

    path = []
    if distances[target] > -math.inf:
        # i = target
        # while i != start:
        #     path.append(i + 1)
        #     i = previous[i]
        # path.append(start + 1)
        # path.reverse()
        # print(path)
        print(distances[target])
    else:
        print('No solution')

