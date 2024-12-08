import time
import numpy as np


def check_antinodes(coords: list(), bounds: tuple):
    nodes = []
    for first_ant in coords:
        for second_ant in coords:
            if first_ant != second_ant:
                x_dist = first_ant[0] - second_ant[0]
                y_dist = first_ant[1] - second_ant[1]
                if 0 <= first_ant[0] + x_dist < bounds[0] and 0 <= first_ant[1] + y_dist < bounds[1]:
                    nodes.append((first_ant[0] + x_dist, first_ant[1] + y_dist))
                if 0 <= second_ant[0] - x_dist < bounds[0] and 0 <= second_ant[1] - y_dist < bounds[1]:
                    nodes.append((second_ant[0] - x_dist, second_ant[1] - y_dist))
    return list(set(nodes))


def check_extended_antinodes(coords: list(), bounds: tuple):
    nodes = []
    for first_ant in coords:
        for second_ant in coords:
            if first_ant != second_ant:
                x_dist = first_ant[0] - second_ant[0]
                y_dist = first_ant[1] - second_ant[1]
                for i in range(bounds[0]):
                    if 0 <= first_ant[0] + i*x_dist < bounds[0] and 0 <= first_ant[1] + i*y_dist < bounds[1]:
                        nodes.append((first_ant[0] + i*x_dist, first_ant[1] + i*y_dist))
                    if 0 <= second_ant[0] - i*x_dist < bounds[0] and 0 <= second_ant[1] - i*y_dist < bounds[1]:
                        nodes.append((second_ant[0] - i*x_dist, second_ant[1] - i*y_dist))
    return list(set(nodes))


def advent8_1():
    #file = open('input08ex.txt'); map_size = (12, 12)
    file = open('input08.txt'); map_size = (50, 50)
    map = np.full(map_size, '.', dtype=str)
    line_num = 0
    antennas = dict()
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] != '.':
                if row[ch] not in antennas.keys():
                    antennas[row[ch]] = list()
                antennas[row[ch]].append([line_num, ch])
        line_num += 1
    sum = 0
    for freq in antennas:
        anti_nodes = check_antinodes(antennas[freq], map_size)
        for n in anti_nodes:
            if map[n] == '.':
                sum += 1
    print('''Nof antinodes:''', sum)


def advent8_2():
    #file = open('input08ex.txt'); map_size = (12, 12)
    file = open('input08.txt'); map_size = (50, 50)
    map = np.full(map_size, '.', dtype=str)
    line_num = 0
    antennas = dict()
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] != '.':
                if row[ch] not in antennas.keys():
                    antennas[row[ch]] = list()
                antennas[row[ch]].append([line_num, ch])
        line_num += 1
    sum = 0
    for freq in antennas:
        anti_nodes = check_extended_antinodes(antennas[freq], map_size)
        for n in anti_nodes:
            map[n] = '#'
    for e in np.nditer(map):
        if e == '#':
            sum += 1
    print('''Nof antinodes:''', sum)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 8')
    advent8_1()
    advent8_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
