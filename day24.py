import time


GATE_NO = 0


class Wire:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def graphviz_output(self):
        descr = self.name + ' [shape=diamond, color=red];\n'
        return descr


class Gate:
    def __init__(self, OP: str, input0: Wire, input1: Wire, output: Wire):
        global GATE_NO
        self.OP = OP
        self.input0 = input0
        self.input1 = input1
        self.output = output
        self.name = 'G' + str(GATE_NO)
        GATE_NO += 1
        
    def calc_output(self):
        if self.input0.value is None:
            return
        if self.input1.value is None:
            return
        if self.OP == 'AND':
            self.output.value = self.input0.value & self.input1.value
        elif self.OP == 'OR':
            self.output.value = self.input0.value | self.input1.value
        elif self.OP == 'XOR':
            self.output.value = self.input0.value ^ self.input1.value

    def graphviz_output(self):
        descr = self.name + '_' + self.OP + ' [shape=box, color=green];\n'
        descr += self.name + '_' + self.OP + ' -> ' + self.output.name + ';\n'
        descr += self.input0.name + ' -> ' + self.name + '_' + self.OP + ';\n'
        descr += self.input1.name + ' -> ' + self.name + '_' + self.OP + ';\n'
        return descr


def advent24_1():
    file = open('input24.txt')
    wires = dict()
    gates = list()
    for line in file:
        if line == '\n':
            break
        wires[line.strip('\n').split(': ')[0]] = Wire(line.strip('\n').split(': ')[0], int(line.strip('\n').split(': ')[1]))
    for line in file:
        line = line.strip('\n')
        left, out = line.split(' -> ')
        in0, OP, in1 = left.split(' ')
        if in0 not in wires.keys():
            wires[in0] = Wire(in0, None)
        if in1 not in wires.keys():
            wires[in1] = Wire(in1, None)
        gates.append(Gate(OP, wires[in0], wires[in1], Wire(out, None)))

    while True:
        any_nones = False
        for g in range(len(gates)):
            gate = gates[g]
            gate.calc_output()
            if gate.output.value is None:
                any_nones = True
            wires[gate.output.name] = gate.output
        for g in range(len(gates)):
            gates[g].input0 = wires[gates[g].input0.name]
            gates[g].input1 = wires[gates[g].input1.name]
        if not any_nones:
            break

    zwires = []
    for gate in gates:
        if gate.output.name[0] == 'z':
            zwires.append(gate.output)

    zwires.sort(key=lambda x: x.name)
    number = 0
    bp = 0
    for zw in zwires:
        number += zw.value*2**bp
        bp += 1
    print('Number:', number)


def advent24_2():
    file = open('input24b.txt')
    # This file contains the swaps
    # These where figured out by inspecting
    # the network (as graphviz dot output)
    # The necessary swaps where:
    # ['z18' <-> 'dhq','z22' <-> 'pdg','z27' <-> 'jcp','kfp' <-> 'hbs']

    wires = dict()
    gates = list()
    for line in file:
        if line == '\n':
            break
        wires[line.strip('\n').split(': ')[0]] = Wire(line.strip('\n').split(': ')[0], int(line.strip('\n').split(': ')[1]))
    for line in file:
        line = line.strip('\n')
        left, out = line.split(' -> ')
        in0, OP, in1 = left.split(' ')
        if in0 not in wires.keys():
            wires[in0] = Wire(in0, None)
        if in1 not in wires.keys():
            wires[in1] = Wire(in1, None)
        gates.append(Gate(OP, wires[in0], wires[in1], Wire(out, None)))

    GRAPHVIZ_FILE = open('system.txt', 'w')
    GRAPHVIZ_FILE.write('digraph {\n')
    for k, wire in wires.items():
        GRAPHVIZ_FILE.write(wire.graphviz_output())
        
    for gate in gates:
        GRAPHVIZ_FILE.write(gate.graphviz_output());
    GRAPHVIZ_FILE.write('}\n')
    
    xwires = []
    ywires = []
    for wire in wires.items():
        if wire[0][0] == 'x':
            xwires.append(wire[1])
        elif wire[0][0] == 'y':
            ywires.append(wire[1])
    xwires.sort(key=lambda x: x.name)
    ywires.sort(key=lambda x: x.name)
    xnumber = 0
    ynumber = 0
    bp = 0
    for xw in xwires:
        xnumber += xw.value*2**bp
        bp += 1
    bp = 0
    for yw in ywires:
        ynumber += yw.value*2**bp
        bp += 1
    print('Addition:', xnumber, '+', ynumber, '=', xnumber + ynumber)
    print('In binary:', str(bin(xnumber + ynumber))[2:])
    
    while True:
        any_nones = False
        for g in range(len(gates)):
            gate = gates[g]
            gate.calc_output()
            if gate.output.value is None:
                any_nones = True
            wires[gate.output.name] = gate.output
        for g in range(len(gates)):
            gates[g].input0 = wires[gates[g].input0.name]
            gates[g].input1 = wires[gates[g].input1.name]
        if not any_nones:
            break

    zwires = []
    for gate in gates:
        if gate.output.name[0] == 'z':
            zwires.append(gate.output)

    zwires.sort(key=lambda x: x.name)
    number = 0
    bp = 0
    for zw in zwires:
        number += zw.value*2**bp
        bp += 1
    print(number)
    print(str(bin(number))[2:])
    print(number - xnumber - ynumber)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 24')
    advent24_1()
    advent24_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
