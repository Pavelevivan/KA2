def reverse_node_edges(node, adj_matrix):
    rev_adj_nodes = [x for x in adj_matrix if x not in adj_matrix[node]
                     and x != node]
    new_matrix = {}
    for x in adj_matrix:
        if x == node:
            for w in adj_matrix[x]:
                if w not in adj_matrix:
                    new_matrix[w] = []
                new_matrix[w].append(x)
        else:
            if node in adj_matrix[x]:
                adj_matrix[x].remove(node)
            new_matrix[x] = adj_matrix[x]
    new_matrix[node] = rev_adj_nodes
    return new_matrix


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
    return adj_matrix, v_to_reverse


def save_result(cur_chain, file='out.txt'):
    with open(file, 'w') as f:
        if len(cur_chain) == len(adj_matrix):
            f.write('{} 1'.format(v))
        else:
            f.write('{} 0'.format(v))


def hamilton_cycle(k):
    if len(cur_chain) == len(adj_matrix) - 1 and v in adj_matrix[k]:
        global stop
        cur_chain[k] = v
        stop = True
    else:
        for x in adj_nodes[k]:
            status[x] = 1
            cur_chain[k] = x
            adj_nodes[x] = [w for w in adj_matrix[x] if not status[w]]
            hamilton_cycle(x)
            if stop:
                break
            status[x] = 0


adj_matrix, v = parse_input()
print(adj_matrix, v)
adj_matrix = reverse_node_edges(v, adj_matrix)

print(adj_matrix)
status = {x: 0 for x in adj_matrix}
status[v] = 1
stop = False
adj_nodes = {v: adj_matrix[v][::]}
print(adj_nodes)
cur_chain = {}
hamilton_cycle(v)
print(cur_chain)
save_result(cur_chain)
