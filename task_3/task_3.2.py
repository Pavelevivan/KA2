def parse_input(file='in.txt'):
    adj_matrix = {}
    with open(file) as f:
        n = int(f.readline())
        for x in range(1, n + 1):
            in_node = [int(v) for v in f.readline().split(' ')[1:]]
            for node in in_node:
                if node not in adj_matrix:
                    adj_matrix[node] = []
                adj_matrix[node].append(x)
        v_to_reverse = int(f.readline())
    for x in range(1, n+1):
        if x not in adj_matrix:
            adj_matrix[x] = []
    return adj_matrix, v_to_reverse


def reverse_node_edges(node):
    rev_adj_nodes = [x for x in adj_matrix if x not in adj_matrix[node]
                     and x != node]
    for x in adj_matrix:
        if node in adj_matrix[x]:
            adj_matrix[x].remove(node)
    for x in adj_matrix:
        if x == node:
            for v in adj_matrix[x]:
                adj_matrix[v].append(x)
    adj_matrix[node] = rev_adj_nodes
    return adj_matrix


def save_result(component_number, file='out.txt'):
    with open(file, 'w') as f:
        if component_number == 1:
            f.write('{} 1'.format(v))
        else:
            f.write('{} 0'.format(v))


def strong_component(v):
    global i
    num[v] = i
    L[v] = i
    i += 1
    stack.append(v)
    for w in adj_matrix[v]:
        if num[w] == -1:
            strong_component(w)
            L[v] = min([L[v], L[w]])
        elif w in stack:
            L[v] = min([L[v], num[w]])
    if L[v] == num[v]:
        while stack and num[stack[-1]] >= num[v]:
            stack.pop()
            # print(stack.pop(), num[v])


adj_matrix, v = parse_input()
print(adj_matrix, v)
reverse_node_edges(v)
print('reversed', adj_matrix)
i = 0
L = {}
stack = []
num = {x: -1 for x in adj_matrix}
for w in num:
    if num[w] == -1:
        strong_component(w)
save_result(len(set(num.keys())))