import time
import numpy as np


class robot:
    def __init__(self, p: tuple, v: tuple, tilesize: tuple):
        self.p = p
        self.v = v
        self.bounds = tilesize

    def update(self):
        self.p = (self.p[0] + self.v[0], self.p[1] + self.v[1])
        self.p = (self.p[0] % self.bounds[0], self.p[1] % self.bounds[1])

    def within(self, bounds: list):
        if bounds[0][0] <= self.p[0] < bounds[0][1] and bounds[1][0] <= self.p[1] < bounds[1][1]:
            return True
        return False


def advent14_1():
    #file = open('input14ex.txt'); tile_size = (7, 11)
    file = open('input14.txt'); tile_size = (103, 101)
    robots = []
    for line in file:
        row = line.strip('\n')
        row = row.split(' ')
        p = row[0][2:].split(',')
        v = row[1][2:].split(',')
        robots.append(robot((int(p[1]), int(p[0])), (int(v[1]), int(v[0])), tile_size))

    t_end = 100
    for t in range(t_end):
        for r in robots:
            r.update()

    quadrant1 = [(0, tile_size[0] // 2), (0, tile_size[1] // 2)]
    quadrant2 = [(tile_size[0] // 2 + 1, tile_size[0]), (0, tile_size[1] // 2)]    
    quadrant3 = [(0, tile_size[0] // 2), (tile_size[1] // 2 + 1, tile_size[1])]
    quadrant4 = [(tile_size[0] // 2 + 1, tile_size[0]), (tile_size[1] // 2 + 1, tile_size[1])]
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for r in robots:
        if r.within(quadrant1):
            q1 += 1
        if r.within(quadrant2):
            q2 += 1
        if r.within(quadrant3):
            q3 += 1
        if r.within(quadrant4):
            q4 += 1

    print('Safety factor:', q1*q2*q3*q4)


def advent14_2():
    file = open('input14.txt'); tile_size = (103, 101)
    robots = []
    for line in file:
        row = line.strip('\n')
        row = row.split(' ')
        p = row[0][2:].split(',')
        v = row[1][2:].split(',')
        robots.append(robot((int(p[1]), int(p[0])), (int(v[1]), int(v[0])), tile_size))

    tiles = np.full(tile_size, '.', dtype=str)
    for r in robots:
        tiles[r.p[0]][r.p[1]] = '*'
    for r in range(tile_size[0]):
        for c in range(tile_size[1]):
            print(tiles[r][c], end='')
        print()
    t_end = 0
    for t in range(t_end):
        print(t)
        tiles = np.full(tile_size, '.', dtype=str)
        for r in robots:
            r.update()
            tiles[r.p[0]][r.p[1]] = '*'
        for r in range(tile_size[0]):
            for c in range(tile_size[1]):
                print(tiles[r][c], end='')
            print()


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 14')
    advent14_1()
    advent14_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
