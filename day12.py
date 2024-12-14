import time
import numpy as np

REGIONS = []


def check_inside(coord: tuple, garden: np.full):
    if coord[0] < 0 or coord[1] < 0:
        return False
    if coord[0] >= garden.shape[0] or coord[1] >= garden.shape[1]:
        return False
    return True


class plot:
    def __init__(self, typ: str, coord: tuple):
        self.typ = typ
        self.coord = coord


class region:
    def __init__(self, typ: str):
        self.typ = typ
        self.plots = []
        self.coords = []
        self.boundary = 0
        self.sides = 0

    def belongs(self, p: plot):
        if p.typ != self.typ:
            return False
        if (p.coord[0]+1, p.coord[1]) in self.coords:
            return True
        if (p.coord[0]-1, p.coord[1]) in self.coords:
            return True
        if (p.coord[0], p.coord[1]+1) in self.coords:
            return True
        if (p.coord[0], p.coord[1]-1) in self.coords:
            return True
        return False

    def part_of(self, p: plot):
        if p.typ != self.typ:
            return False
        if (p.coord[0], p.coord[1]) in self.coords:
            return True
        return False

    def add(self, p: plot):
        self.plots.append(p)
        self.coords.append(p.coord)

    def calc_boundary(self):
        for p in self.plots:
            bound = 4
            if (p.coord[0]+1, p.coord[1]) in self.coords:
                bound -= 1
            if (p.coord[0]-1, p.coord[1]) in self.coords:
                bound -= 1
            if (p.coord[0], p.coord[1]+1) in self.coords:
                bound -= 1
            if (p.coord[0], p.coord[1]-1) in self.coords:
                bound -= 1
            self.boundary += bound

    def count_sides(self):
        # find corners
        if len(self.plots) in [1, 2]:
            total_corners = 4
            self.sides = total_corners
            return
        else:
            total_corners = 0
        # outer corners
        for p in self.plots:
            if (p.coord[0]+1, p.coord[1]) not in self.coords:
                if (p.coord[0], p.coord[1]+1) not in self.coords:
                    total_corners += 1
                    if (p.coord[0]-1, p.coord[1]) not in self.coords:
                        total_corners += 1
                if (p.coord[0], p.coord[1]-1) not in self.coords:
                    total_corners += 1
                    if (p.coord[0]-1, p.coord[1]) not in self.coords:
                        total_corners += 1
                continue
            if (p.coord[0]-1, p.coord[1]) not in self.coords:
                if (p.coord[0], p.coord[1]+1) not in self.coords:
                    total_corners += 1
                    if (p.coord[0]+1, p.coord[1]) not in self.coords:
                        total_corners += 1
                if (p.coord[0], p.coord[1]-1) not in self.coords:
                    total_corners += 1
                    if (p.coord[0]+1, p.coord[1]) not in self.coords:
                        total_corners += 1
                continue
            if (p.coord[0], p.coord[1]+1) not in self.coords:
                if (p.coord[0]+1, p.coord[1]) not in self.coords:
                    total_corners += 1
                    if (p.coord[0], p.coord[1]-1) not in self.coords:
                        total_corners += 1
                if (p.coord[0]-1, p.coord[1]) not in self.coords:
                    total_corners += 1
                    if (p.coord[0], p.coord[1]-1) not in self.coords:
                        total_corners += 1
                continue
            if (p.coord[0], p.coord[1]-1) not in self.coords:
                if (p.coord[0]+1, p.coord[1]) not in self.coords:
                    total_corners += 1
                    if (p.coord[0], p.coord[1]+1) not in self.coords:
                        total_corners += 1
                if (p.coord[0]-1, p.coord[1]) not in self.coords:
                    total_corners += 1
                    if (p.coord[0], p.coord[1]+1) not in self.coords:
                        total_corners += 1
                continue
        # inner corners
        for p in self.plots:
            if (p.coord[0]+1, p.coord[1]) in self.coords and (p.coord[0], p.coord[1]+1) in self.coords and (p.coord[0]+1, p.coord[1]+1) not in self.coords:
                total_corners += 1
            if (p.coord[0]-1, p.coord[1]) in self.coords and (p.coord[0], p.coord[1]+1) in self.coords and (p.coord[0]-1, p.coord[1]+1) not in self.coords:
                total_corners += 1
            if (p.coord[0]+1, p.coord[1]) in self.coords and (p.coord[0], p.coord[1]-1) in self.coords and (p.coord[0]+1, p.coord[1]-1) not in self.coords:
                total_corners += 1
            if (p.coord[0]-1, p.coord[1]) in self.coords and (p.coord[0], p.coord[1]-1) in self.coords and (p.coord[0]-1, p.coord[1]-1) not in self.coords:
                total_corners += 1
            
        self.sides = total_corners


def check_plot(garden: np.full, p: plot):
    global REGIONS
    for reg in REGIONS:
        if reg.part_of(p):
            return
    for reg in REGIONS:
        if reg.belongs(p):
            reg.add(p)
            if check_inside((p.coord[0]+1, p.coord[1]), garden) and p.typ == garden[p.coord[0]+1][p.coord[1]]:
                np = plot(garden[p.coord[0]+1][p.coord[1]], (p.coord[0]+1, p.coord[1]))
                check_plot(garden, np)
            if check_inside((p.coord[0]-1, p.coord[1]), garden) and p.typ == garden[p.coord[0]-1][p.coord[1]]:
                np = plot(garden[p.coord[0]-1][p.coord[1]], (p.coord[0]-1, p.coord[1]))
                check_plot(garden, np)
            if check_inside((p.coord[0], p.coord[1]+1), garden) and p.typ == garden[p.coord[0]][p.coord[1]+1]:
                np = plot(garden[p.coord[0]][p.coord[1]+1], (p.coord[0], p.coord[1]+1))
                check_plot(garden, np)
            if check_inside((p.coord[0], p.coord[1]-1), garden) and p.typ == garden[p.coord[0]][p.coord[1]-1]:
                np = plot(garden[p.coord[0]][p.coord[1]-1], (p.coord[0], p.coord[1]-1))
                check_plot(garden, np)
            return
    nr = region(p.typ)
    nr.add(p)
    REGIONS.append(nr)
    if check_inside((p.coord[0]+1, p.coord[1]), garden) and p.typ == garden[p.coord[0]+1][p.coord[1]]:
        np = plot(garden[p.coord[0]+1][p.coord[1]], (p.coord[0]+1, p.coord[1]))
        check_plot(garden, np)
    if check_inside((p.coord[0]-1, p.coord[1]), garden) and p.typ == garden[p.coord[0]-1][p.coord[1]]:
        np = plot(garden[p.coord[0]-1][p.coord[1]], (p.coord[0]-1, p.coord[1]))
        check_plot(garden, np)
    if check_inside((p.coord[0], p.coord[1]+1), garden) and p.typ == garden[p.coord[0]][p.coord[1]+1]:
        np = plot(garden[p.coord[0]][p.coord[1]+1], (p.coord[0], p.coord[1]+1))
        check_plot(garden, np)
    if check_inside((p.coord[0], p.coord[1]-1), garden) and p.typ == garden[p.coord[0]][p.coord[1]-1]:
        np = plot(garden[p.coord[0]][p.coord[1]-1], (p.coord[0], p.coord[1]-1))
        check_plot(garden, np)


def find_regions(garden: np.full):
    for r in range(garden.shape[0]):
        for s in range(garden.shape[1]):
            p = plot(garden[r][s], (r, s))
            check_plot(garden, p)


def advent12_1():
    global REGIONS
    # file = open('input12ex.txt'); garden_size = (4, 4)
    # file = open('input12ex2.txt'); garden_size = (10, 10)
    # file = open('input12ex3.txt'); garden_size = (5, 5)
    file = open('input12.txt'); garden_size = (140, 140)
    garden = np.full(garden_size, '.', dtype=str)
    line_num = 0
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            garden[line_num, ch] = row[ch]
        line_num += 1
    find_regions(garden)
    tot_cost = 0
    for r in REGIONS:
        r.calc_boundary()
        cost = r.boundary*len(r.plots)
        tot_cost += cost
    print('Fence cost(i):', tot_cost)


def advent12_2():
    global REGIONS
    # file = open('input12ex.txt'); garden_size = (4, 4)
    # file = open('input12ex2.txt'); garden_size = (10, 10)
    # file = open('input12ex3.txt'); garden_size = (5, 5)
    file = open('input12.txt'); garden_size = (140, 140)
    garden = np.full(garden_size, '.', dtype=str)
    line_num = 0
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            garden[line_num, ch] = row[ch]
        line_num += 1
    find_regions(garden)
    tot_cost = 0
    for r in REGIONS:
        r.count_sides()
        cost = r.sides*len(r.plots)
        tot_cost += cost
    print('Fence cost(ii):', tot_cost)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 12')
    advent12_1()
    advent12_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
