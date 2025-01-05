import time


def advent13_1():
    file = open('input13.txt')
    tokens = 0
    while True:
        nums1 = file.readline().strip('\n').split(':')
        nums2 = file.readline().strip('\n').split(':')
        nums3 = file.readline().strip('\n').split(':')
        file.readline()
        if len(nums1) == 1:
            break
        a11 = int(nums1[1].split(', ')[0].lstrip(' ')[2:])
        a12 = int(nums2[1].split(', ')[0].lstrip(' ')[2:])
        a21 = int(nums1[1].split(', ')[1].lstrip(' ')[2:])
        a22 = int(nums2[1].split(', ')[1].lstrip(' ')[2:])
        b1 = int(nums3[1].split(', ')[0].lstrip(' ')[2:])
        b2 = int(nums3[1].split(', ')[1].lstrip(' ')[2:])
        y = (b2 - b1*a21/a11) / (a22 - a12*a21/a11)
        x = (b1 - a12*y) / a11
        if abs(x - int(round(x))) < 0.01 and abs(y - int(round(y))) < 0.01 and x < 101 and y < 101:
            tokens += 3*x + y

    print('Tokens(i):', tokens)


def advent13_2():
    file = open('input13.txt')
    tokens = 0
    while True:
        nums1 = file.readline().strip('\n').split(':')
        nums2 = file.readline().strip('\n').split(':')
        nums3 = file.readline().strip('\n').split(':')
        file.readline()
        if len(nums1) == 1:
            break
        a11 = int(nums1[1].split(', ')[0].lstrip(' ')[2:])
        a12 = int(nums2[1].split(', ')[0].lstrip(' ')[2:])
        a21 = int(nums1[1].split(', ')[1].lstrip(' ')[2:])
        a22 = int(nums2[1].split(', ')[1].lstrip(' ')[2:])
        b1 = int(nums3[1].split(', ')[0].lstrip(' ')[2:]) + 10000000000000
        b2 = int(nums3[1].split(', ')[1].lstrip(' ')[2:]) + 10000000000000
        y = (b2 - b1*a21/a11) / (a22 - a12*a21/a11)
        x = (b1 - a12*y) / a11
        if abs(x - int(round(x))) < 0.01 and abs(y - int(round(y))) < 0.01:
            tokens += 3*x + y

    print('Tokens(ii):', tokens)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 13')
    advent13_1()
    advent13_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
