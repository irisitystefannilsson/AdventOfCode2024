import time
import itertools


NUMPAD = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
          '4': (1, 0), '5': (1, 1), '6': (1, 2),
          '1': (2, 0), '2': (2, 1), '3': (2, 2),
          '0': (3, 1), 'A': (3, 2)}


DIRPAD = {'^': (0, 1), 'A': (0, 2),
          '<': (1, 0), 'v': (1, 1), '>': (1, 2)}


MOVE_MAP = {'A<': 'v<<A',
            '<A': '>>^A',
            'A^': '<A',
            '^A': '>A',
            'A>': 'vA',
            '>A': '^A',
            'Av': '<vA',
            'vA': '^>A',
            '>^': '<^A',
            '^>': '>vA',
            '>v': '<A',
            'v>': '>A',
            '<v': '>A',
            'v<': '<A',
            '<^': '>^A',
            '^<': 'v<A'}


COST_CACHE = dict()


def check_if_ok(moves: str, padtype: str):
    numforbid = (3, 0)
    dirforbid = (0, 0)
    pos = NUMPAD['A'] if padtype == 'num' else DIRPAD['A']
    forbidden = numforbid if padtype == 'num' else dirforbid
    for m in moves:
        if m == 'A':
            continue
        if m == 'v':
            pos = (pos[0] + 1, pos[1])
        elif m == '^':
            pos = (pos[0] - 1, pos[1])
        elif m == '>':
            pos = (pos[0], pos[1] + 1)
        elif m == '<':
            pos = (pos[0], pos[1] - 1)
        if pos == forbidden:
            return False
    return True


def generate_syms(syms: str, padtype: str):
    vars = {''}
    symlist = syms.split('A')
    for var in symlist:
        newvars = set()
        for comb in itertools.permutations(var):
            for elem in vars:
                newvars.add(elem + ''.join(comb) + 'A')
        vars = newvars.copy()
    retvars = set()
    for var in vars:
        if check_if_ok(var, padtype):
            retvars.add(var[:-1])
    return retvars


def make_next_lvl_move(move: str):
    global DIRPAD
    pos = move[0]
    moves = ''
    for l in range(1, len(move)):
        let = move[l]
        if pos == let:
            moves += 'A'
        else:
            moves += MOVE_MAP[pos + let]
        pos = let
    return moves


def recurse_until_done(depth: int, move: str, max_depth: int):
    global COST_CACHE
    if (move, depth) in COST_CACHE.keys():
        return COST_CACHE[(move, depth)]
    next_move = make_next_lvl_move(move)
    depth += 1
    if depth == max_depth:
        return len(next_move)
    else:
        combos = generate_syms(next_move, 'dir')
        min_len = 1e100
        for combo in combos:
            rec_len = 0
            next_move = 'A' + combo
            sub_moves = next_move.split('A')
            for s in range(1, len(sub_moves) - 1):
                sub_move = 'A' + sub_moves[s] + 'A'
                rec_len += recurse_until_done(depth, sub_move, max_depth)
            min_len = min(min_len, rec_len)
            
        COST_CACHE[(move, depth - 1)] = min_len
        return min_len


def advent21_1():
    global NUMPAD
    global DIRPAD
    global opt_seqs
    file = open('input21.txt')
    codes = []
    for line in file:
        code = line.strip('\n')
        codes.append(code)

    complexity = 0
    for code in codes:
        moves0 = ''
        pos_0 = NUMPAD['A']
        for dig in code:
            newpos = NUMPAD[dig]
            diff = (newpos[0] - pos_0[0], newpos[1] - pos_0[1])
            pos_0 = newpos
            moves0 += 'v'*diff[0] if diff[0] > 0 else '^'*abs(diff[0])
            moves0 += '>'*diff[1] if diff[1] > 0 else '<'*abs(diff[1])
            moves0 += 'A'
            combos0 = generate_syms(moves0, 'num')
        seq_len = 100000000000
        for combo0 in combos0:
            pos_1 = DIRPAD['A']
            moves1 = ''
            for sym in combo0:
                newpos = DIRPAD[sym]
                diff = (newpos[0] - pos_1[0], newpos[1] - pos_1[1])
                pos_1 = newpos
                moves1 += 'v'*diff[0] if diff[0] > 0 else '^'*abs(diff[0])
                moves1 += '>'*diff[1] if diff[1] > 0 else '<'*abs(diff[1])
                moves1 += 'A'
            combos1 = generate_syms(moves1, 'dir')
            for combo1 in combos1:
                pos_2 = DIRPAD['A']
                moves2 = ''
                for sym in combo1:
                    newpos = DIRPAD[sym]
                    diff = (newpos[0] - pos_2[0], newpos[1] - pos_2[1])
                    pos_2 = newpos
                    moves2 += 'v'*diff[0] if diff[0] > 0 else '^'*abs(diff[0])
                    moves2 += '>'*diff[1] if diff[1] > 0 else '<'*abs(diff[1])
                    moves2 += 'A'
                if not check_if_ok(moves2, 'dir'):
                    pos_2 = DIRPAD['A']
                    moves2 = ''
                    for sym in combo1:
                        newpos = DIRPAD[sym]
                        diff = (newpos[0] - pos_2[0], newpos[1] - pos_2[1])
                        pos_2 = newpos
                        moves2 += '>'*diff[1] if diff[1] > 0 else '<'*abs(diff[1])
                        moves2 += 'v'*diff[0] if diff[0] > 0 else '^'*abs(diff[0])
                        moves2 += 'A'

                if seq_len > len(moves2):
                    seq_len = len(moves2)
        complexity += seq_len * int(code[:-1])

    print('Complexity(i):', complexity)


def advent21_2():
    global NUMPAD
    global opt_seqs
    file = open('input21.txt')
    codes = []
    for line in file:
        code = line.strip('\n')
        codes.append(code)

    nof_rounds = 25
    complexity = 0
    for code in codes:
        moves0 = ''
        pos_0 = NUMPAD['A']
        for dig in code:
            newpos = NUMPAD[dig]
            diff = (newpos[0] - pos_0[0], newpos[1] - pos_0[1])
            pos_0 = newpos
            moves0 += 'v'*diff[0] if diff[0] > 0 else '^'*abs(diff[0])
            moves0 += '>'*diff[1] if diff[1] > 0 else '<'*abs(diff[1])
            moves0 += 'A'
        combos0 = generate_syms(moves0, 'num')
        minlen = 1e100
        for combo in combos0:
            mlen = recurse_until_done(0, 'A' + combo, nof_rounds)
            minlen = min(minlen, mlen)
        complexity += minlen*int(code[:-1])

    print('Complexity(ii):', complexity)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 21')
    advent21_1()
    advent21_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
