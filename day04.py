import time
import numpy as np

def findall(s, p):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    sum = 0
    while i != -1:
        sum += 1
        i = s.find(p, i + 1)
    return sum


def findall_return_pos(s, p):
    '''Yields all the positions of
    the pattern p in the string s.'''
    pos = []
    i = s.find(p)
    while i != -1:
        pos.append(i + 1)
        i = s.find(p, i + 1)
    return pos


def find_word(board: np.full, word: str):
    sum = 0
    board_size = board.shape
    bword = word[::-1]
    for r in range(board_size[0]):
        # rows
        row = board[r, :]
        str_row = ''
        for s in range(board_size[1]):
            str_row += row[s]
        sum += findall(str_row, word)
        sum += findall(str_row, bword)
    for s in range(board_size[1]):
        # columns
        col = board[:, s]
        str_col = ''
        for r in range(board_size[0]):
            str_col += col[r]
        sum += findall(str_col, word)
        sum += findall(str_col, bword)
    # diags, starting from upper left, and lower right (square board assumed
    for r in range(board_size[0]):
        diags_ul = ''
        diags_lr = ''
        for s in range(r + 1):
            diags_ul += board[r - s, s]
            diags_lr += board[board_size[0] - 1 - s, board_size[0] - 1 - r + s] 
        sum += findall(diags_ul, word)
        sum += findall(diags_ul, bword)
        if r != board_size[0] - 1:
            sum += findall(diags_lr, word)
            sum += findall(diags_lr, bword)
    # diags, starting from lower left, and upper right (square board assumed
    for r in range(board_size[0]):
        diags_ll = ''
        diags_ur = ''
        for s in range(r + 1):
            diags_ll += board[board_size[0] - 1 - r + s, s]
            diags_ur += board[s, board_size[0] - 1 - r + s]
        sum += findall(diags_ll, word)
        sum += findall(diags_ll, bword)
        if r != board_size[0] - 1:
            sum += findall(diags_ur, word)
            sum += findall(diags_ur, bword) 
    return sum


def find_crossword(board: np.full, word: str):
    sum = 0
    board_size = board.shape
    bword = word[::-1]
    coords = []
    # diags, starting from upper left, and lower right (square board assumed
    for r in range(board_size[0]):
        diags_ul = ''
        diags_lr = ''
        for s in range(r + 1):
            diags_ul += board[r - s, s]
            diags_lr += board[board_size[0] - 1 - s, board_size[0] - 1 - r + s] 
        pos = findall_return_pos(diags_ul, word)
        for p in pos:
            coords.append([r - p, p])
        pos = findall_return_pos(diags_ul, bword)
        for p in pos:
            coords.append([r - p, p])
        if r != board_size[0] - 1:
            pos = findall_return_pos(diags_lr, word)
            for p in pos:
                coords.append([board_size[0] - 1 - p, board_size[0] - 1 - r + p])
            pos = findall_return_pos(diags_lr, bword)
            for p in pos:
                coords.append([board_size[0] - 1 - p, board_size[0] - 1 - r + p])
    # diags, starting from lower left, and upper right (square board assumed
    for r in range(board_size[0]):
        diags_ll = ''
        diags_ur = ''
        for s in range(r + 1):
            diags_ll += board[board_size[0] - 1 - r + s, s]
            diags_ur += board[s, board_size[0] - 1 - r + s]
        pos = findall_return_pos(diags_ll, word)
        for p in pos:
            coords.append([board_size[0] - 1 - r + p, p])
        pos = findall_return_pos(diags_ll, bword)
        for p in pos:
            coords.append([board_size[0] - 1 - r + p, p])
        if r != board_size[0] - 1:
            pos = findall_return_pos(diags_ur, word)
            for p in pos:
                coords.append([p, board_size[0] - 1 - r + p])
            pos = findall_return_pos(diags_ur, bword)
            for p in pos:
                coords.append([p, board_size[0] - 1 - r + p])
    for c in range(len(coords)):
        for d in range(c + 1, len(coords)):
            if coords[c] == coords[d]:
                 sum += 1
        
    return sum


def advent4_1():
    #file = open('input04ex.txt'); board_size = (10, 10)
    file = open('input04.txt'); board_size = (140, 140)
    board = np.full(board_size, '.', dtype=str)
    line_num = 0
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            board[line_num, ch] = row[ch]
        line_num += 1
    word = 'XMAS'
    sum = find_word(board, word)
    print('Nof XMAS:', sum)


def advent4_2():
    #file = open('input04ex.txt'); board_size = (10, 10)
    file = open('input04.txt'); board_size = (140, 140)
    board = np.full(board_size, '.', dtype=str)
    line_num = 0
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            board[line_num, ch] = row[ch]
        line_num += 1
    word = 'MAS'
    sum = find_crossword(board, word)
    print('Nof X-MAS:', sum)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 4')
    advent4_1()
    advent4_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
