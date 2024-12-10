import time
import numpy as np


ALL_ENDS = []


def on_map(map: np.full, step: tuple):
    if step[0] < 0 or step[1] < 0:
        return False
    if step[0] >= map.shape[0] or step[1] >= map.shape[1]:
        return False
    return True


def calc_next(map: np.full, start: tuple, curr: int):
    next_steps = [(start[0]+1, start[1]), (start[0]-1, start[1]), (start[0], start[1]+1), (start[0], start[1]-1)]
    for step in next_steps:
        if on_map(map, step) and map[step] == curr + 1:
            if curr == 8:
                ALL_ENDS.append(step)
            else:
                calc_next(map, step, curr + 1)


def advent10_1():
    global ALL_ENDS
    #file = open('input10ex.txt'); map_size = (4, 4)
    #file = open('input10ex2.txt'); map_size = (8, 8)
    file = open('input10.txt'); map_size = (41, 41)
    map = np.full(map_size, 0, dtype=int)
    line_num = 0
    trailheads = [] 
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = int(row[ch])
            if int(row[ch]) == 0:
                trailheads.append((line_num, ch))
        line_num += 1

    sum = 0
    for start in trailheads:
        calc_next(map, start, 0)
        sum += len(set(ALL_ENDS))
        ALL_ENDS = []
        
    print('''Trailhead score(i):''', sum)


def advent10_2():
    global ALL_ENDS
    ALL_ENDS = []
    #file = open('input10ex.txt'); map_size = (4, 4)
    #file = open('input10ex2.txt'); map_size = (8, 8)
    file = open('input10.txt'); map_size = (41, 41)
    map = np.full(map_size, 0, dtype=int)
    line_num = 0
    trailheads = [] 
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = int(row[ch])
            if int(row[ch]) == 0:
                trailheads.append((line_num, ch))
        line_num += 1

    for start in trailheads:
        calc_next(map, start, 0)
        
    print('''Trailhead score(ii):''', len(ALL_ENDS))


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 10')
    advent10_1()
    advent10_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
