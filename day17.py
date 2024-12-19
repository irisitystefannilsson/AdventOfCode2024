import time


RA = 0
RB = 0
RC = 0
PPTR = 0


def combo_operand(operand: int):
    global RA
    global RB
    global RC
    if operand < 4:
        return operand
    if operand == 4:
        return RA
    if operand == 5:
        return RB
    if operand == 6:
        return RC
    raise


def advance_program(opcode: int, operand: int):
    global RA
    global RB
    global RC
    global PPTR
    # time.sleep(0.1)
    if opcode == 0:  # adv
        numerator = RA
        denominator = 2**combo_operand(operand)
        RA = numerator // denominator
        PPTR += 2
        return
    if opcode == 1:  # bxl
        RB = RB ^ operand
        PPTR += 2
        return
    if opcode == 2:  # bst
        RB = combo_operand(operand) % 8
        PPTR += 2
        return
    if opcode == 3:  # jnz
        if RA == 0:
            PPTR += 2
            return
        else:
            PPTR = operand
            return
    if opcode == 4:  # bxc
        RB = RB ^ RC
        PPTR += 2
        return
    if opcode == 5:  # out
        print(combo_operand(operand) % 8, end=',')
        PPTR += 2
        return
    if opcode == 6:  # bdv
        numerator = RA
        denominator = 2**combo_operand(operand)
        RB = numerator // denominator
        PPTR += 2
        return
    if opcode == 7:  # cdv
        numerator = RA
        denominator = 2**combo_operand(operand)
        RC = numerator // denominator
        PPTR += 2
        return


def advent17_1():
    global RA
    global RB
    global RC
    global PPTR
    file = open('input17.txt')
    program = None
    for line in file:
        if 'Register A' in line:
            RA = int(line.split(': ')[1].strip('\n')) 
        elif 'Register B' in line:
            RB = int(line.split(': ')[1].strip('\n'))
        elif 'Register C' in line:
            RC = int(line.split(': ')[1].strip('\n'))
        elif 'Program' in line:
            program = line.strip('\n').split(': ')[1]
            program = [int(e) for e in program.split(',')]

    print('Output : ', end='')
    while PPTR < len(program):
        advance_program(program[PPTR], program[PPTR + 1])
    print()


def advent17_2():
    # The program loops until RA is 0
    # RA  --> RA // 8 every loop
    # Every loop will output RB % 8
    # RB will be equal to :
    # (((RA % 8)^1)^RC)^6
    # where RC = RA // 2**((RA % 8)^1)
    # Testing gives the value of RB at the
    # last output as RB=4
    # From there I worked backwards (by hand)
    # as: RA --> RA*8 + x where x = [0..7]
    # until all output was correct.
    # Starting RA = 247839002892474
    # N.B. there where sometimes more than
    # one x giving the correct output, I
    # had to try multiple paths at sometime
    # outputs
    global RA
    global RB
    global RC
    global PPTR
    file = open('input17.txt')
    program = None
    for line in file:
        if 'Register A' in line:
            RA = int(line.split(': ')[1].strip('\n'))
        elif 'Register B' in line:
            RB = int(line.split(': ')[1].strip('\n'))
        elif 'Register C' in line:
            RC = int(line.split(': ')[1].strip('\n'))
        elif 'Program' in line:
            program = line.strip('\n').split(': ')[1]
            program = [int(e) for e in program.split(',')]
    for p in program:
        print(p, end=',')
    print()
    while PPTR < len(program):
        advance_program(program[PPTR], program[PPTR + 1])
    print()


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 17')
    advent17_1()
    advent17_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
