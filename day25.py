import time


def key_fits(key: list, lock: list):
    for t in range(5):
        if key[t] + lock[t] > 5:
            return False
    return True


def advent25_1():
    file = open('input25.txt')
    locks = []
    keys = []
    nrows = 0
    while True:
        nrows += 1
        line = file.readline()
        if not line:
            break
        if line[0] == '#':  # lock
            lock = [0, 0, 0, 0, 0]
            for r in range(1, 7):
                line = file.readline()
                line.strip('\n')
                for c in range(5):
                    if line[c] == '#':
                        lock[c] += 1
            locks.append(lock)
        elif line[0] == '.':  # key
            key = [-1, -1, -1, -1, -1]
            for r in range(1, 7):
                line = file.readline()
                line.strip('\n')
                for c in range(5):
                    if line[c] == '#':
                        key[c] += 1
            keys.append(key)
    print('Nof locks:', len(locks))
    print('Nof keys:', len(keys))
    nof_fits = 0
    for key in keys:
        for lock in locks:
            if key_fits(key, lock):
                nof_fits += 1
    print('Nof fits:', nof_fits)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 25')
    advent25_1()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
