import time
import numpy as np
import networkx as nx


def inside(bounds: tuple, r, c):
    if r < 0 or c < 0:
        return False
    if r >= bounds[0] or c >= bounds[1]:
        return False
    return True


def build_graph(memory: np.full):
    G = nx.Graph()
    for r in range(memory.shape[0]):
        for c in range(memory.shape[1]):
            if memory[r][c] == '.':
                G.add_node((r, c))
    for r in range(memory.shape[0]):
        for c in range(memory.shape[1]):
            if memory[r][c] == '.':
                nr, nc = r + 1, c
                if inside(memory.shape, nr, nc) and memory[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc))
                nr, nc = r - 1, c
                if inside(memory.shape, nr, nc) and memory[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc))
                nr, nc = r, c + 1
                if inside(memory.shape, nr, nc) and memory[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc))
                nr, nc = r, c - 1
                if inside(memory.shape, nr, nc) and memory[nr][nc] == '.':
                    G.add_edge((r, c), (nr, nc))

    return G


def advent18_1():
    # file = open('input18ex.txt'); mem_size = (7, 7); mem_lim = 12
    file = open('input18.txt'); mem_size = (71, 71); mem_lim = 1024
    memory = np.full(mem_size, '.', dtype=str)
    start = (0, 0)
    goal = (mem_size[0] - 1, mem_size[1] - 1)
    count = 0
    for line in file:
        row = line.strip('\n')
        c, r = row.split(',')
        memory[int(r)][int(c)] = '#'
        count += 1
        if count == mem_lim:
            break
    mem_graph = build_graph(memory)
    path = nx.shortest_path(mem_graph, start, goal)
    print('Min. no of steps:', len(path) - 1)


def advent18_2():
    # file = open('input18ex.txt'); mem_size = (7, 7); mem_lim = 12
    file = open('input18.txt'); mem_size = (71, 71); mem_lim = 1024
    memory = np.full(mem_size, '.', dtype=str)
    start = (0, 0)
    goal = (mem_size[0] - 1, mem_size[1] - 1)
    count = 0
    for line in file:
        row = line.strip('\n')
        c, r = row.split(',')
        memory[int(r)][int(c)] = '#'
        count += 1
        if count == mem_lim:
            break
    mem_graph = build_graph(memory)
    for line in file:
        row = line.strip('\n')
        c, r = row.split(',')
        c, r = int(c), int(r)
        mem_graph.remove_node((r, c))
        try:
            nx.shortest_path(mem_graph, start, goal)
        except Exception:
            print('No path at', c, r)
            break


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 18')
    advent18_1()
    advent18_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
