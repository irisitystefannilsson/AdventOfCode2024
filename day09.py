import time


def first_free(disk: list):
    for i in range(len(disk)):
        if disk[i] == '.':
            return i
    return -1


def last_nonfree(disk: list):
    for i in reversed(range(len(disk))):
        if disk[i] != '.':
            return i
    return -1


def compactify(disk: list()):
    while True:
        ff = first_free(disk)
        lnf = last_nonfree(disk)
        if ff > lnf:
            break
        disk[ff], disk[lnf] = disk[lnf], disk[ff]


def last_disk(disk: list, file_id: str):
    for i in reversed(range(len(disk))):
        if disk[i] == file_id:
            e = i
            break
    for i in range(len(disk)):
        if disk[i] == file_id:
            s = i
            break
    return s, e


def first_large_enough_free(disk: list, req: int):
    for i in range(len(disk)):
        if disk[i] == '.':
            s = i
            for j in range(i + 1, len(disk)):
                if disk[j] != '.':
                    if j - s >= req:
                        return s
                    else:
                        break
    return -1


def smart_compactify(disk: list()):
    last_file_id = disk[len(disk) - 1]
    while int(last_file_id) > 0:
        s, e = last_disk(disk, last_file_id)
        ff = first_large_enough_free(disk, e - s + 1)
        if ff != -1 and s > ff:
            for i in range(e - s + 1):
                disk[ff + i], disk[s + i] = disk[s + i], disk[ff + i]
        last_file_id = str(int(last_file_id) - 1)


def calc_checksum(disk: list):
    sum = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            sum += i*int(disk[i])
    return sum


def advent9_1():
    file = open('input09.txt')
    disk = []
    disk_map = file.read().strip('\n')
    file_id = 0
    is_file = True
    for num in disk_map:
        if is_file:
            for i in range(int(num)):
                disk.append(str(file_id))
            is_file = False
            file_id += 1
        else:
            for i in range(int(num)):
                disk.append('.')
            is_file = True
    compactify(disk)
    checksum = calc_checksum(disk)
    print('CHKSum (i): ', checksum)


def advent9_2():
    file = open('input09.txt')
    disk = []
    disk_map = file.read().strip('\n')
    file_id = 0
    is_file = True
    for num in disk_map:
        if is_file:
            for i in range(int(num)):
                disk.append(str(file_id))
            is_file = False
            file_id += 1
        else:
            for i in range(int(num)):
                disk.append('.')
            is_file = True
    smart_compactify(disk)
    checksum = calc_checksum(disk)
    print('CHKSum (ii) : ', checksum)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 9')
    advent9_1()
    advent9_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
