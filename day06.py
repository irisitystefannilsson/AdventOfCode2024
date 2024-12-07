import time
import numpy as np


def move_guard(map: np.full, start: list):
    m_index = 0
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    pos = start
    new_pos = pos
    while True:
        new_pos = [pos[0] + moves[m_index][0], pos[1] + moves[m_index][1]]
        try:
            if map[new_pos[0]][new_pos[1]] == '#':
                m_index = (m_index + 1) % 4
            else:
                pos = new_pos
                map[pos[0]][pos[1]] = 'x'
        except Exception:
            break
    return map


def count_x(map: np.full):
    sum = 0
    for e in np.nditer(map):
        if e == 'x':
            sum += 1
    return sum


def closed_circuit(map: np.full, start: list):
    m_index = 0
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dirs = ['^', '>', 'v', '<']
    used_states = dict()
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            used_states[i, j] = []
    pos = start
    used_states[pos[0], pos[1]].append(dirs[m_index])
    new_pos = pos
    while True:
        new_pos = [pos[0] + moves[m_index][0], pos[1] + moves[m_index][1]]
        #print(new_pos)
        try:
            if map[new_pos[0]][new_pos[1]] == '#':
                m_index = (m_index + 1) % 4
            else:
                pos = new_pos
                if dirs[m_index] in used_states[new_pos[0], new_pos[1]]:
                    #print(dirs[m_index], pos, used_states[new_pos[0], new_pos[1]])
                    #print(map)
                    return True
                else:
                    used_states[new_pos[0], new_pos[1]].append(dirs[m_index])
        except Exception:
            #print(used_states)
            return False


def advent6_1():
    #file = open('input06ex.txt'); map_size = (10, 10)
    file = open('input06.txt'); map_size = (130, 130)
    map = np.full(map_size, '.', dtype=str)
    line_num = 0
    guard_start = [-1, -1]
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] == '^':
                guard_start = [line_num, ch]
        line_num += 1

    map = move_guard(map, guard_start)
    sum = count_x(map)
    print('''Nof X's:''', sum)


def advent6_2():
    #file = open('input06ex.txt'); map_size = (10, 10)
    file = open('input06.txt'); map_size = (130, 130)
    map = np.full(map_size, '.', dtype=str)
    line_num = 0
    guard_start = [-1, -1]
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] == '^':
                guard_start = [line_num, ch]
        line_num += 1
    sum = 0
    for i in range(map_size[0]):
        for j in range(map_size[1]):
            orig_char = map[i][j]
            map[i][j] = '#'
            #print(map)
            if closed_circuit(map, guard_start):
                sum += 1
            map[i][j] = orig_char
    print('''Nof CC's:''', sum)

if __name__ == '__main__':

    start_time = time.time()
    print('Advent 6')
    advent6_1()
    advent6_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
