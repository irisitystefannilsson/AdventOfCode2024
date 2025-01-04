import time


def blink(stones: list):
    new_stones = []
    for stone in stones:
        if int(stone) == 0:
            stone = '1'
            new_stones.append(stone)
        elif len(stone) % 2 == 0:
            stone, new_stone = stone[0:int(len(stone)/2)], stone[int(len(stone)/2):]
            new_stones.append(stone)
            new_stone = new_stone.lstrip('0')
            if new_stone == '':
                new_stone = '0'
            new_stones.append(new_stone)
        else:
            stone = str(int(stone)*2024)
            new_stones.append(stone)
    return new_stones


def advent11_1():
    file = open('input11.txt')
    stones = file.read().strip('\n').split(' ')
    nof_blinks = 25
    old_len = len(stones)
    old_diff = 0
    print(0, old_len, 0, 0)
    for b in range(nof_blinks):
        stones = blink(stones)
        diff = len(stones) - old_len
        #print(stones)
        print(b + 1, len(stones), diff, diff - old_diff)
        old_len = len(stones)
        old_diff = diff
    print('Nof stones: ', len(stones))


def advent11_2():
    file = open('input11.txt')
    stones = file.read().strip('\n').split(' ')
    nof_blinks = 25
    for b in range(nof_blinks):
        stones = blink(stones)
        print(b + 1, len(stones))

    print('Nof stones(25):', len(stones))

    sorted_stones = dict()
    for stone in stones:
        sorted_stones[stone] = sorted_stones.get(stone, 0) + 1

    nof_stones = 0
    more_sorted_stones = dict()
    for stone_type in sorted_stones.keys():
        stones2nd = [stone_type]    
        for b in range(nof_blinks):
            stones2nd = blink(stones2nd)
        nof_stones += sorted_stones[stone_type]*len(stones2nd)
        for stone in stones2nd:
            more_sorted_stones[stone] = more_sorted_stones.get(stone, 0) + sorted_stones[stone_type]
    print('Nof stones(50):', nof_stones)
    # print(len(more_sorted_stones.keys()))

    nof_stones = 0
    for stone_type in more_sorted_stones.keys():
        stones3rd = [stone_type]    
        for b in range(nof_blinks):
            stones3rd = blink(stones3rd)
        nof_stones += more_sorted_stones[stone_type]*len(stones3rd)
    print('Nof stones(75):', nof_stones)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 1')
    # advent11_1()
    advent11_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
