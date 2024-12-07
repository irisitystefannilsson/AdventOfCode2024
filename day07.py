import time
import itertools


def possible(result: int, operands: list):
    nof_operators = len(operands) - 1
    for operators in itertools.product('+*', repeat=nof_operators):
        tmp_res = 0
        if operators[0] == '+':
            tmp_res = int(operands[0]) + int(operands[1])
        else:
            tmp_res = int(operands[0]) * int(operands[1])
        for i in range(1, nof_operators):
            if operators[i] == '+':
                tmp_res += int(operands[i + 1])
            else:
                tmp_res *= int(operands[i + 1])
        if tmp_res == result:
            return True
    return False


def further_possible(result: int, operands: list):
    nof_operators = len(operands) - 1
    for operators in itertools.product('+*|', repeat=nof_operators):
        tmp_res = 0
        if operators[0] == '+':
            tmp_res = int(operands[0]) + int(operands[1])
        elif operators[0] == '*':
            tmp_res = int(operands[0]) * int(operands[1])
        else:
            tmp_res = int(operands[0] + operands[1])
        for i in range(1, nof_operators):
            if operators[i] == '+':
                tmp_res += int(operands[i + 1])
            elif operators[i] == '*':
                tmp_res *= int(operands[i + 1])
            else:
                tmp_res = int(str(tmp_res) + operands[i + 1])
        if tmp_res == result:
            return True
    return False


def advent7_1():
    file = open('input07.txt')
    results = []
    operands = []
    for line in file:
        line = line.strip('\n')
        split_line = line.split(':')
        results.append(int(split_line[0]))
        operands.append(split_line[1].lstrip(' ').split(' '))
    sum = 0
    for i in range(len(results)):
        if possible(results[i], operands[i]):
            sum += results[i]
    print('Sum : ', sum)


def advent7_2():
    file = open('input07.txt')
    results = []
    operands = []
    for line in file:
        line = line.strip('\n')
        split_line = line.split(':')
        results.append(int(split_line[0]))
        operands.append(split_line[1].lstrip(' ').split(' '))
    sum = 0
    for i in range(len(results)):
        if further_possible(results[i], operands[i]):
            sum += results[i]
    print('Sum : ', sum)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 7')
    advent7_1()
    advent7_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
