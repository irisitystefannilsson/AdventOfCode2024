import time

POSSIBLE = []
IMPOSSIBLE = set()
NOF_OPTIONS = 0
POSSIBLE_MAP = dict()


def check_possibility(design: str, patterns: list):
    global POSSIBLE
    global IMPOSSIBLE
    if design in POSSIBLE:
        return True
    if design in IMPOSSIBLE:
        return False
    possible = False
    for pattern in patterns:
        if design == pattern:
            return True
        if design.find(pattern) == 0:
            possible = check_possibility(design[len(pattern):], patterns)
            if possible:
                break
    if possible:
        POSSIBLE.append(design)
    else:
        IMPOSSIBLE.add(design)
    return possible


def check_all_possibilities(design: str, patterns: list, indent=''):
    global POSSIBLE_MAP
    global IMPOSSIBLE
    global NOF_OPTIONS
    if design in POSSIBLE_MAP:
        NOF_OPTIONS += POSSIBLE_MAP[design]
        return True
    if design in IMPOSSIBLE:
        return False
    for_possible = False
    possible = False
    for pattern in patterns:
        if design == pattern:
            possible = True
            for_possible = True
            NOF_OPTIONS += 1
            POSSIBLE_MAP[design] = POSSIBLE_MAP.get(design, 0) + 1
        elif design.find(pattern) == 0:
            possible = check_all_possibilities(design[len(pattern):], patterns)
            if possible:
                POSSIBLE_MAP[design] = POSSIBLE_MAP.get(design, 0) + POSSIBLE_MAP[design[len(pattern):]]
                for_possible = True
    if for_possible:
        pass
    else:
        IMPOSSIBLE.add(design)
    return for_possible


def advent19_1():
    file = open('input19.txt')
    available = file.readline().strip('\n').split(', ')
    file.readline()
    designs = []
    for line in file:
        designs.append(line.strip('\n'))
    nof_possible = 0
    for design in designs:
        possible = check_possibility(design, available)
        if possible:
            nof_possible += 1
    print('Nof possible designs(i):', nof_possible)


def advent19_2():
    global NOF_OPTIONS
    global POSSIBLE

    file = open('input19.txt')
    available = file.readline().strip('\n').split(', ')
    file.readline()
    designs = []
    for line in file:
        designs.append(line.strip('\n'))
    for design in designs:
        check_all_possibilities(design, available)
    print('Total nof possible designs(ii):', NOF_OPTIONS)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 19')
    advent19_1()
    advent19_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
