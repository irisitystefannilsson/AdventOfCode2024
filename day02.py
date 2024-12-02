import time

def safe_increase(report: list):
    for i in range(len(report) - 1):
        if (report[i + 1] - report[i]) < 1 or (report[i + 1] - report[i]) > 3:
            return False
    return True

def safe_decrease(report: list):
    for i in range(len(report) - 1):
        if (report[i] - report[i + 1]) < 1 or (report[i] - report[i + 1]) > 3:
            return False
    return True

def advent2_1():
    file = open('input02.txt')
    nof_safe_reports = 0
    for line in file:
        nums = line.split()
        report = [int(e) for e in nums]
        if safe_increase(report) or safe_decrease(report):
            nof_safe_reports += 1

    print('Nof Safe reports:', nof_safe_reports)


def advent2_2():
    file = open('input02.txt')
    nof_safe_reports = 0
    for line in file:
        nums = line.split()
        report = [int(e) for e in nums]
        if safe_increase(report) or safe_decrease(report):
            nof_safe_reports += 1
        else:
            for l in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(l)
                if safe_increase(report_copy) or safe_decrease(report_copy):
                    nof_safe_reports += 1
                    break

    print('Nof Safe reports:', nof_safe_reports)
    

if __name__ == '__main__':

    start_time = time.time()
    print('Advent 2')
    advent2_1()
    advent2_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
