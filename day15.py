import time
import sys
import numpy as np


MOVE_CONV = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

CRATES = []

MOVABLES = []


def copy_walls(warehouse: np.full):
    for r in range(warehouse.shape[0]):
        for c in range(warehouse.shape[1]):
            if warehouse[r][c] in ['[', ']', '@']:
                warehouse[r][c] = '.'


def crate_movable(warehouse: np.full, pos: tuple, dir:tuple):
    for crate in CRATES:
        if crate.on(pos):
            return crate.movable(warehouse, dir)
    return True


class robot:
    def __init__(self, pos):
        self.pos = pos

    def movable(self, warehouse: np.full, dir: tuple):
        if warehouse[self.pos[0] + dir[0]][self.pos[1] + dir[1]] == '#':
            return False
        elif warehouse[self.pos[0] + dir[0]][self.pos[1] + dir[1]] == '.':
            return True
        else:
            return crate_movable(warehouse, (self.pos[0] + dir[0], self.pos[1] + dir[1]), dir)

    def move(self, dir: tuple):
        self.pos = (self.pos[0] + dir[0], self.pos[1] + dir[1])

    def mark(self, warehouse: np.full):
        warehouse[self.pos[0]][self.pos[1]] = '@'


class crate:
    def __init__(self, pos: tuple):
        self.pos = pos

    def on(self, pos: tuple):
        if pos == self.pos or pos == (self.pos[0], self.pos[1] + 1):
            return True
        return False
        
    def movable(self, warehouse: np.full, dir: tuple):
        MOVABLES.append(self)
        if dir[1] == 1 and warehouse[self.pos[0]][self.pos[1] + 2] == '#':
            return False
        elif dir[1] == 1 and warehouse[self.pos[0]][self.pos[1] + 2] == '.':
            return True
        elif dir[1] == -1 and warehouse[self.pos[0]][self.pos[1] - 1] == '#':
            return False
        elif dir[1] == -1 and warehouse[self.pos[0]][self.pos[1] - 1] == '.':
            return True
        elif warehouse[self.pos[0] + dir[0]][self.pos[1]] == '#' or warehouse[self.pos[0] + dir[0]][self.pos[1] + 1] == '#':
            return False
        elif warehouse[self.pos[0] + dir[0]][self.pos[1]] == '.' and warehouse[self.pos[0] + dir[0]][self.pos[1] + 1] == '.':
            return True
        else:
            if dir[1] == 0:
                return crate_movable(warehouse, (self.pos[0] + dir[0], self.pos[1] + dir[1]), dir) and crate_movable(warehouse, (self.pos[0] + dir[0], self.pos[1] + 1 + dir[1]), dir)
            else:
                if dir[1] == -1:
                    return crate_movable(warehouse, (self.pos[0] + dir[0], self.pos[1] + dir[1]), dir)
                else:
                    return crate_movable(warehouse, (self.pos[0] + dir[0], self.pos[1] + 1 + dir[1]), dir)

    def mark(self, warehouse: np.full):
        warehouse[self.pos[0]][self.pos[1]] = '['
        warehouse[self.pos[0]][self.pos[1]+1] = ']'

    def move(self, dir: tuple):
        self.pos = (self.pos[0] + dir[0], self.pos[1] + dir[1])

    def gps_cost(self, warehouse: np.full):
        rowdist = self.pos[0]
        coldist = self.pos[1]
        return rowdist*100 + coldist


def empty_space(warehouse: np.full, pos: tuple, dir: tuple):
    new_p = pos
    while True:
        new_p = (new_p[0] + dir[0], new_p[1] + dir[1])
        if warehouse[new_p[0]][new_p[1]] == '.':
            return new_p
        elif warehouse[new_p[0]][new_p[1]] == '#':
            return pos


def move_robot(warehouse: np.full, pos: tuple, dir: tuple):
    space_p = empty_space(warehouse, pos, dir)
    if space_p == pos:
        return pos
    while space_p != pos:
        n_space_p = (space_p[0] - dir[0], space_p[1] - dir[1])
        warehouse[n_space_p[0]][n_space_p[1]], warehouse[space_p[0]][space_p[1]] = warehouse[space_p[0]][space_p[1]], warehouse[n_space_p[0]][n_space_p[1]]
        space_p = n_space_p
    return (pos[0] + dir[0], pos[1] + dir[1])


def gps_sum(warehouse: np.full):
    sum = 0
    for r in range(warehouse.shape[0]):
        for c in range(warehouse.shape[1]):
            if warehouse[r][c] == 'O':
                sum += r*100 + c
    return sum


def advent15_1():
    # file = open('input15ex2.txt'); warehouse_size = (8, 8)
    # file = open('input15ex.txt'); warehouse_size = (10, 10)
    file = open('input15.txt'); warehouse_size = (50, 50)
    warehouse = np.full(warehouse_size, '.', dtype=str)
    robot_pos = (0, 0)
    r = 0
    for line in file:
        if line == '\n':
            break
        row = line.strip('\n')
        for c in range(len(row)):
            warehouse[r][c] = row[c]
            if row[c] == '@':
                robot_pos = (r, c)
        r += 1
    moves = []
    for line in file:
        row = line.strip('\n')
        for c in range(len(row)):
            moves.append(row[c])
    for m in moves:
        robot_pos = move_robot(warehouse, robot_pos, MOVE_CONV[m])
    gpss = gps_sum(warehouse)
    print('Gps_Sum(i):', gpss)


def advent15_2():
    global MOVABLES
    # file = open('input15ex2.txt'); warehouse_size = (8, 8*2)
    # file = open('input15ex.txt'); warehouse_size = (10, 10*2)
    file = open('input15.txt'); warehouse_size = (50, 50*2)
    warehouse = np.full(warehouse_size, '.', dtype=str)
    robot_pos = (0, 0)
    rob = robot(robot_pos)
    r = 0
    for line in file:
        if line == '\n':
            break
        row = line.strip('\n')
        for c in range(len(row)):
            if row[c] == '#':
                warehouse[r][2*c] = '#'
                warehouse[r][2*c+1] = '#'
            elif row[c] == 'O':
                warehouse[r][2*c] = '['
                warehouse[r][2*c+1] = ']'
                CRATES.append(crate((r, 2*c)))
            elif row[c] == '.':
                warehouse[r][2*c] = '.'
                warehouse[r][2*c+1] = '.'
            elif row[c] == '@':
                robot_pos = (r, 2*c)
                rob = robot(robot_pos)
                warehouse[r][2*c] = '@'
                warehouse[r][2*c+1] = '.'
        r += 1
    moves = []
    for line in file:
        row = line.strip('\n')
        for c in range(len(row)):
            moves.append(row[c])
    np.set_printoptions(threshold=sys.maxsize, linewidth=100)
    for m in moves:
        if rob.movable(warehouse, MOVE_CONV[m]):
            rob.move(MOVE_CONV[m])
            MOVABLES = list(set(MOVABLES))
            for c in MOVABLES:
                c.move(MOVE_CONV[m])
        copy_walls(warehouse)
        rob.mark(warehouse)
        for c in CRATES:
            c.mark(warehouse)
        MOVABLES = []

    gpss = 0
    for c in CRATES:
        gpss += c.gps_cost(warehouse)
    print('Gps_Sum(i):', gpss)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 15')
    advent15_1()
    advent15_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
