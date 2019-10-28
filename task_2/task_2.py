import math


def make_graph_m(adj_matrix, second_part, x_double, y_double, dx, dy):
    graph = {(x, y): 0 for x in adj_matrix
             for y in y_double}
    dx = set()
    dy = set()
    front_x = {x: math.inf for x in adj_matrix}
    front_y = {y: math.inf for y in second_part}
    queue_1 = []
    queue_2 = []
    x_free = []
    y_free = []
    for x in adj_matrix:
        if x_double[x] is None:
            queue_2.append(x)
            x_free.append(x)
            dx.add(x)
            front_x[x] = 0
        queue_1, queue_2 = queue_2, []
        while queue_1:
            x = queue_1.pop()
            for y in second_part:
                if y in adj_matrix[x] and front_x[x] < front_y[y]:
                    graph[(x, y)] = 1
                    if front_y[y] == math.inf:
                        dy.add(y)
                        z = y_double[y]
                        if z:
                            graph[(z, y)] = 1
                            dx.add(x)
                            front_x[x] = front_y[y] + 1
                            queue_2.append(x)
                        else:
                            y_free.append(y)
    return x_double, y_double, graph


def increase(x_double, y_double, dx, dy):
    pass


def hopkroft_karp(adj_matrix, second_part):
    x_double = {x: None for x in adj_matrix}
    y_double = {y: None for y in second_part}
    x_free = [0]
    y_free = [0]
    dx = []
    dy = []
    while y_free:
        x_double, y_double, graph = make_graph_m(adj_matrix, second_part, x_double, y_double, dx, dy)
        print(x_free, y_free, graph)
        if y_free:
            increase(x_free, y_free, dx, dy)


def create_second_part(matching):
    return {x + 1: matching[x] for x in range(len(matching))}


def convert_to_matching(int_lists, second_part):
    uniq_numbers = set(x for int_list in int_lists
                       for x in int_list)

    adj_matrix = {}
    for num in uniq_numbers:
        adj_matrix[num] = []
        for key, value in second_part.items():
            if num in value:
                adj_matrix[num].append(key)

    return adj_matrix


def parse_input():
    int_lists = []
    with open('in.txt') as f:
        list_num = int(f.readline())
        for x in range(list_num):
            num_set = [int(x) for x in f.readline() if x.isdigit() and int(x)]
            int_lists.append(num_set)
    return int_lists


def save_result(max_matching):
    pass


if __name__ == '__main__':
    int_lists = parse_input()
    print(int_lists)
    second_part = create_second_part(int_lists)
    print(second_part)
    matching = convert_to_matching(int_lists, second_part)
    print(matching)
    max_matching = hopkroft_karp(matching, second_part)

    # save_result(max_matching)