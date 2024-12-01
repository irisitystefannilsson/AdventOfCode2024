import time


def advent1_1():
    file = open('input01.txt')
    id1 = list()
    id2 = list()
    for line in file:
        nums = line.split()
        id1.append(int(nums[0]))
        id2.append(int(nums[1]))

    id1.sort()
    id2.sort()
    sum = 0
    for i in range(len(id1)):
        sum += abs(id1[i] - id2[i])
    print('Sum : ', sum)


def advent1_2():
    file = open('input01.txt')
    id1 = list()
    id2 = list()
    for line in file:
        nums = line.split()
        id1.append(int(nums[0]))
        id2.append(int(nums[1]))

    sim_score = 0
    for i in range(len(id1)):
        for j in range(len(id2)):
            if id2[j] == id1[i]:
                sim_score += id1[i]

    print('Similarity score:', sim_score)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 1')
    advent1_1()
    advent1_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
