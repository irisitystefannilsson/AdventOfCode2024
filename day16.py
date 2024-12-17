import time
import numpy as np
import networkx as nx


DIST = -1


def is_node(coord: tuple, maze: np.full):
    if maze[coord[0]][coord[1]] == '#':
        return False
    if maze[coord[0]+1][coord[1]] == '.' and maze[coord[0]][coord[1]+1] == '.':
        return True
    if maze[coord[0]-1][coord[1]] == '.' and maze[coord[0]][coord[1]+1] == '.':
        return True
    if maze[coord[0]+1][coord[1]] == '.' and maze[coord[0]][coord[1]-1] == '.':
        return True
    if maze[coord[0]-1][coord[1]] == '.' and maze[coord[0]][coord[1]-1] == '.':
        return True
    return False


def fillin_path(path, maze: np.full):
    for node_no in range(len(path) - 1):
        coord1 = path[node_no]
        coord2 = path[node_no + 1]
        if coord1[0] == coord2[0]:
            low = min(coord1[1], coord2[1])
            hi = max(coord1[1], coord2[1])
            maze[coord1[0]][low:hi+1] = 'O'
        else:
            low = min(coord1[0], coord2[0])
            hi = max(coord1[0], coord2[0])
            maze[low:hi+1][:, coord1[1]] = 'O'


def free_path(coord1: tuple, coord2: tuple, maze: np.full):
    global DIST
    if coord1[0] == coord2[0]:
        low = min(coord1[1], coord2[1])
        hi = max(coord1[1], coord2[1])
        if np.all(maze[coord1[0]][low:hi] == '.'):
            DIST = hi - low
            return True
    if coord1[1] == coord2[1]:
        low = min(coord1[0], coord2[0])
        hi = max(coord1[0], coord2[0])
        if np.all(maze[low:hi][:, coord1[1]] == '.'):
            DIST = hi - low
            return True
    return False


def build_graph(maze: np.full, start: tuple, goal: tuple):
    global DIST
    nodes = []
    for r in range(1, maze.shape[0] - 1):
        for c in range(1, maze.shape[1] - 1):
            if is_node((r, c), maze):
                nodes.append((r, c))
    if start not in nodes:
        nodes.append(start)
    if goal not in nodes:
        nodes.append(goal)
    G = nx.Graph()
    for node in nodes:
        G.add_node(node)
    used_edges = []
    start_row = start[0]
    for s_node in nodes:
        for node in nodes:
            if s_node != node and free_path(s_node, node, maze) and (node, s_node) not in used_edges:
                if (node == start or s_node == start) and node[0] == start_row:
                    G.add_edge(s_node, node, weight=DIST)
                else:
                    G.add_edge(s_node, node, weight=DIST+1000)
                used_edges.append((s_node, node))
    return G


def advent16_1():
    # file = open('input16ex.txt'); maze_size = (15, 15)
    # file = open('input16ex2.txt'); maze_size = (17, 17)
    file = open('input16.txt'); maze_size = (141, 141)
    maze = np.full(maze_size, '.', dtype=str)
    start = (-1, -1)
    goal = (-1, -1)
    r = 0
    for line in file:
        row = line.strip('\n')
        for c in range(len(row)):
            maze[r][c] = row[c]
            if row[c] == 'S':
                start = (r, c)
            if row[c] == 'E':
                goal = (r, c)
        r += 1
    maze[start[0]][start[1]] = '.'
    maze[goal[0]][goal[1]] = '.'
    maze_graph = build_graph(maze, start, goal)
    path = nx.shortest_path(maze_graph, start, goal, weight='weight')
    print(path)
    cost = nx.path_weight(maze_graph, path, weight='weight')
    print('Min cost is:', cost)
    return cost


def advent16_2(min_cost: int):
    # file = open('input16ex.txt'); maze_size = (15, 15)
    # file = open('input16ex2.txt'); maze_size = (17, 17)
    file = open('input16.txt'); maze_size = (141, 141)
    maze = np.full(maze_size, '.', dtype=str)
    start = (-1, -1)
    goal = (-1, -1)
    r = 0
    for line in file:
        row = line.strip('\n')
        for c in range(len(row)):
            maze[r][c] = row[c]
            if row[c] == 'S':
                start = (r, c)
            if row[c] == 'E':
                goal = (r, c)
        r += 1
    maze[start[0]][start[1]] = '.'
    maze[goal[0]][goal[1]] = '.'
    maze_graph = build_graph(maze, start, goal)
    maze[start[0]][start[1]] = 'O'
    maze[goal[0]][goal[1]] = 'O'
    for path in nx.all_shortest_paths(maze_graph, start, goal):
        cost = nx.path_weight(maze_graph, path, weight='weight')
        if cost == min_cost:
            fillin_path(path, maze)
    print('Tiles in best path(s)', np.count_nonzero(maze == 'O'))


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 16')
    min_cost = advent16_1()
    advent16_2(min_cost)
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
