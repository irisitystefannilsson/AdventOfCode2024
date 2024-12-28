import time
import numpy as np
import networkx as nx


def manhattans(orig: tuple, cpu: np.full, dist: int):
    rets = set()
    for r in range(-dist, dist + 1):
        for c in range(-dist, dist + 1):
            if abs(r) + abs(c) == dist:
                if inside(cpu.shape, orig[0] + r, orig[1] + c) and cpu[orig[0] + r][orig[1] + c] == '.':
                    rets.add((orig[0] + r, orig[1] + c))
    return rets


def inside(bounds: tuple, r: int, c: int):
    if r < 0 or c < 0:
        return False
    if r >= bounds[0] or c >= bounds[1]:
        return False
    return True


def build_graph(cpu: np.full):
    G = nx.Graph()
    for r in range(cpu.shape[0]):
        for c in range(cpu.shape[1]):
            if cpu[r][c] == '.':
                G.add_node((r, c))
    for r in range(cpu.shape[0]):
        for c in range(cpu.shape[1]):
            if cpu[r][c] == '.':
                nr, nc = r + 1, c
                if inside(cpu.shape, nr, nc) and cpu[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc), weight=1)
                nr, nc = r - 1, c
                if inside(cpu.shape, nr, nc) and cpu[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc), weight=1)
                nr, nc = r, c + 1
                if inside(cpu.shape, nr, nc) and cpu[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc), weight=1)
                nr, nc = r, c - 1
                if inside(cpu.shape, nr, nc) and cpu[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc), weight=1)

    return G


def advent20_1():
    # file = open('input20ex.txt'); cpu_size = (15, 15); lim = 0
    file = open('input20.txt'); cpu_size = (141, 141); lim = 100
    cpu = np.full(cpu_size, '.', dtype=str)
    start = (0, 0)
    goal = (0, 0)
    r = 0
    for line in file:
        row = line.strip('\n')
        for c in range(cpu_size[1]):
            cpu[r][c] = row[c]
            if cpu[r][c] == 'S':
                start = (r, c)
                cpu[r][c] = '.'
            if cpu[r][c] == 'E':
                goal = (r, c)
                cpu[r][c] = '.'
        r += 1

    cpu_graph = build_graph(cpu)
    path = nx.shortest_path(cpu_graph, start, goal)
    picos = len(path) - 1
    print('Time [ps]:', picos)
    cheats = dict()
    for r in range(1, cpu_size[0] - 1):
        for c in range(1, cpu_size[1] - 1):
            if cpu[r][c] == '#' and cpu[r + 1][c] == '.' and cpu[r - 1][c] == '.':
                cheat_graph = cpu_graph.copy()
                cheat_graph.add_node((r, c))
                cheat_graph.add_edge((r, c), (r + 1, c))
                cheat_graph.add_edge((r, c), (r - 1, c))
                cheat_path = nx.shortest_path(cheat_graph, start, goal)
                if len(cheat_path) - 1 + lim <= picos:
                    saved = picos + 1 - len(cheat_path)
                    cheats[saved] = cheats.get(saved, 0) + 1
            if cpu[r][c] == '#' and cpu[r][c + 1] == '.' and cpu[r][c - 1] == '.':
                cheat_graph = cpu_graph.copy()
                cheat_graph.add_node((r, c))
                cheat_graph.add_edge((r, c), (r, c + 1))
                cheat_graph.add_edge((r, c), (r, c - 1))
                cheat_path = nx.shortest_path(cheat_graph, start, goal)
                if len(cheat_path) - 1 + lim <= picos:
                    saved = picos + 1 - len(cheat_path)
                    cheats[saved] = cheats.get(saved, 0) + 1
    total = 0
    for nof in cheats.items():
        total += nof[1]
    print('Total cheats(i):', total)


def advent20_2():
    # file = open('input20ex.txt'); cpu_size = (15, 15); lim = 50
    file = open('input20.txt'); cpu_size = (141, 141); lim = 100
    cpu = np.full(cpu_size, '.', dtype=str)
    start = (-1, -1)
    goal = (-1, -1)
    r = 0
    for line in file:
        row = line.strip('\n')
        for c in range(cpu_size[1]):
            cpu[r][c] = row[c]
            if cpu[r][c] == 'S':
                start = (r, c)
                cpu[r][c] = '.'
            if cpu[r][c] == 'E':
                goal = (r, c)
                cpu[r][c] = '.'
        r += 1

    cpu_graph = build_graph(cpu)
    paths = nx.shortest_path(cpu_graph, target=goal)
    picos = len(paths[start]) - 1
    print('Time [ps]:', picos)
    all_pairs = set()
    for r in range(cpu_size[0]):
        for c in range(cpu_size[1]):
            if cpu[r][c] == '.':
                for d in range(2, 21):
                    scnds = manhattans((r, c), cpu, d)
                    for scnd in scnds:
                        edge = ((r, c), scnd, d)
                        all_pairs.add(edge)

    nof_cheats = 0
    for edge in all_pairs:
        start_cost = len(paths[edge[0]]) - 1
        end_cost = len(paths[edge[1]]) - 1
        saved = start_cost - end_cost - edge[2]
        if saved >= lim:
            nof_cheats += 1
    print('Total cheats(ii):', nof_cheats)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 20')
    advent20_1()
    advent20_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
