import time
import networkx as nx


def advent23_1():
    file = open('input23.txt')
    computers = set()
    lan = nx.Graph()
    for line in file:
        pc1, pc2 = line.strip('\n').split('-')
        if pc1 not in computers:
            lan.add_node(pc1)
            computers.add(pc1)
        if pc2 not in computers:
            lan.add_node(pc2)
            computers.add(pc2)
        lan.add_edge(pc1, pc2)
    triads = set()
    for n in lan.nodes():
        neighbors = set()
        for nn in lan.neighbors(n):
            neighbors.add(nn)
        for nnn in neighbors:
            for nnnn in lan.neighbors(nnn):
                if nnnn in neighbors:
                    lt = [n, nnn, nnnn]
                    lt.sort()
                    triads.add(tuple(lt))

    nof_t_triads = 0
    for t in triads:
        if t[0][0] == 't' or t[1][0] == 't' or t[2][0] == 't':
            nof_t_triads += 1
    print('Nof triads with t:', nof_t_triads)


def advent23_2():
    file = open('input23.txt')
    computers = set()
    lan = nx.Graph()
    for line in file:
        pc1, pc2 = line.strip('\n').split('-')
        if pc1 not in computers:
            lan.add_node(pc1)
            computers.add(pc1)
        if pc2 not in computers:
            lan.add_node(pc2)
            computers.add(pc2)
        lan.add_edge(pc1, pc2)
    cliques = list(nx.enumerate_all_cliques(lan))
    cliques.sort(key=len, reverse=True, )
    passwd = list()
    for n in cliques[0]:
        passwd.append(n)
    passwd.sort()
    for p in passwd:
        print(p, end=',')
    print()


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 23')
    advent23_1()
    advent23_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
