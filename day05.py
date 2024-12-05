import time


def advent5_1():
    file = open('input05.txt')
    before = list()
    after = list()
    for i in range(100):
        before.append([])
        after.append([])
    page_collection = list()
    for line in file:
        line = line.strip('\n')
        if line.find('|') != -1:
            b, a = line.split('|')
            before[int(a)].append(int(b))
            after[int(b)].append(int(a))
        elif line.find(',') != -1:
            page_collection.append(line.split(','))
    sum = 0

    disordered = []
    for pages in page_collection:
        ordering_ok = True
        for i in range(len(pages)):
            for j in range(i):
                if int(pages[j]) in after[int(pages[i])]:
                    ordering_ok = False
            for j in range(i + 1, len(pages)):
                if int(pages[j]) in before[int(pages[i])]:
                    ordering_ok = False
        if ordering_ok:
            sum += int(pages[int(len(pages)/2)])
        else:
            disordered.append(pages)
    print('Sum (i): ', sum)
    advent5_2(disordered, before, after)

    
def advent5_2(disordered_page_collection: list, before: list, after: list):
    sum = 0
    for pages in disordered_page_collection:
        ordering_ok = False
        while not ordering_ok:
            try:
                for i in range(len(pages)):
                    for j in range(i):
                        if int(pages[j]) in after[int(pages[i])]:
                            pages[j], pages[i] = pages[i], pages[j]
                            raise
                    for j in range(i, len(pages)):
                        if int(pages[j]) in before[int(pages[i])]:
                            pages[j], pages[i] = pages[i], pages[j]
                            raise Exception
                ordering_ok = True
            except Exception:
                pass

        if ordering_ok:
            sum += int(pages[int(len(pages)/2)])
    print('Sum (ii):', sum)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 5')
    advent5_1()  # calls Advent5_2
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
