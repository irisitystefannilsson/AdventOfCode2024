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
    nof_blinks = 15
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
    pass


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 1')
    advent11_1()
    #advent11_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
