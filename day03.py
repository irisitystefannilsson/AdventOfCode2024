import time

def verify_mul(expression: str):
    pos = 3
    if expression[pos] != '(':
        return 0
    pos += 1
    comma = expression[pos:].find(',')
    if comma < 1 or comma > 3:
        return 0
    if not expression[pos:pos+comma].isdigit():
        return 0
    first_term = int(expression[pos:pos+comma])
    pos += comma + 1
    end_paran = expression[pos:].find(')')
    if end_paran < 1 or end_paran > 3:
        return 0
    if not expression[pos:pos+end_paran].isdigit():
        return 0
    second_term = int(expression[pos:pos+end_paran])
    pos += end_paran
    prod = first_term * second_term
    return prod


def advent3_1():
    file = open('input03.txt')
    sum = 0
    for line in file:
        for pos in range(len(line)):
            if line[pos:pos+3] == 'mul':
                sum += verify_mul(line[pos:])

    print('Sum of muls (i):', sum)


def advent3_2():
    file = open('input03.txt')
    sum = 0
    enabled = True
    for line in file:
        for pos in range(len(line)):
            if line[pos:pos+3] == 'mul':
                if enabled:
                    sum += verify_mul(line[pos:])
            elif line[pos:pos+4] == 'do()':
                enabled = True
            elif line[pos:pos+7] == '''don't()''':
                enabled = False

    print('Sum of muls (ii):', sum)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 3')
    advent3_1()
    advent3_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
