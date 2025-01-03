import time


def pseudo(num: int):
    mixres = num * 64
    num = num ^ mixres
    num = num % 16777216
    mixres = num // 32
    num = num ^ mixres
    num = num % 16777216
    mixres = num * 2048
    num = num ^ mixres
    num = num % 16777216
    return num


def advent22_1():
    file = open('input22.txt')
    start_numbers = []
    for line in file:
        num = int(line.strip('\n'))
        start_numbers.append(num)
        
    nof_new_nums = 2000
    final_numbers = []
    pseudo_sum = 0
    for num in start_numbers:
        new_num = num
        for iter in range(nof_new_nums):
            new_num = pseudo(new_num)
        final_numbers.append(new_num)
        # print(num, ':', new_num)
        pseudo_sum += new_num
    print('Sum of pseudos:', pseudo_sum)


def advent22_2():
    file = open('input22.txt')
    start_numbers = []
    for line in file:
        num = int(line.strip('\n'))
        start_numbers.append(num)
        
    nof_new_nums = 2000
    price_changes = []
    idx = 0
    for num in start_numbers:
        price_changes.append([])
        new_num = num
        price_changes[idx].append(int(str(new_num)[-1]))
        for iter in range(nof_new_nums):
            new_num = pseudo(new_num)
            price_changes[idx].append(int(str(new_num)[-1]))
        idx += 1

    sequences = dict()
    b = 0
    for buyer in price_changes:
        for ch in range(4, len(buyer)):
            change = (buyer[ch - 3] - buyer[ch - 4], buyer[ch - 2] - buyer[ch - 3], buyer[ch - 1] - buyer[ch - 2], buyer[ch] - buyer[ch - 1])
            if change in sequences.keys():
                sequences[change].append((b, buyer[ch]))
            else:
                sequences[change] = [(b, buyer[ch])]
        b += 1
    max_bananas = 0
    for seq in sequences.keys():
        bananas = 0
        used = set()
        for b in sequences[seq]:
            if b[0] in used:
                continue
            else:
                bananas += b[1]
                used.add(b[0])
        max_bananas = max(max_bananas, bananas)
    print('Bananas:', max_bananas)
    

if __name__ == '__main__':

    start_time = time.time()
    print('Advent 22')
    advent22_1()
    advent22_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
