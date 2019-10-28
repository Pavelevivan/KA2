def parse_input():
    int_lists = []
    with open('in.txt') as f:
        list_num = int(f.readline())
        for x in range(list_num):
            num_set = [int(x) for x in f.readline() if x.isdigit() and int(x)]
            int_lists.append(num_set)
    return int_lists


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


def create_second_part(matching):
    return {x + 1: matching[x] for x in range(len(matching))}


def save_result(res):
    with open('out.txt', 'w') as f:
        if res:
            for v, e in res:
                f.write(f"{v}\n")


def kuhn(v):
    if v not in visited:
        visited.add(v)
        for to in cs[v]:
            if mt[to] == -1 or kuhn(mt[to]):
                mt[to], res[v] = v, to
                return 1
        return 0


int_list = parse_input()
u = create_second_part(int_list)
# print(int_list)
# print(u)
v = convert_to_matching(int_list, u)
# print(v)
# n, k = int(input()), int(input())
# cs = [[j for j, e in enumerate(input().split()) if e == '1'] for i in range(n)]
cs = v
mt, res = {x: -1 for x in u}, {x: -1 for x in v}
# print(mt, res)
for v in cs:
    visited = set()
    kuhn(v)
# print(res)

res = res if len(res) == len(u) else []
res = [(v, e) for v, e in res.items()]
res.sort(key=lambda x: x[1])
save_result(res)
# print(" ".join(f"{v, e}\n" for v, e in res if e > 0))