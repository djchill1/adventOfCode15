from unittest import TestCase
import numpy as np
import re

with open('7_input.txt') as fp:
    data = fp.read().splitlines()


def split_input(data):
    instructions = []
    for instruction in data:
        parsed = re.split(" ", instruction, 6)
        instructions.append(parsed)
    return instructions




def part_a(instructions):
    parsed = split_input(instructions)
    dict = {}
    executors = ['AND', 'OR', 'LSHIFT', 'RSHIFT']
    for instruction in parsed:
        print(instruction)
        try:
            if instruction[1] == '->':
                print('setting', instruction[2], 'to',  instruction[0])
                if instruction[0].isdigit() is True:
                    dict[instruction[2]] = np.uint16(int(instruction[0]))
                else:
                    dict[instruction[2]] = np.uint16(int(dict[instruction[0]]))
                print('set dict:', dict)
            elif instruction[1] in executors:
                if instruction[0].isdigit() is True:
                    val1 = int(instruction[0])
                else:
                    val1 = dict[instruction[0]]
                print(val1)
                if instruction[2].isdigit() is True:
                    val2 = int(instruction[2])
                else:
                    val2 = dict[instruction[2]]
                print(val2)
                if instruction[1] == 'AND':
                    dict[instruction[4]] = np.uint16(int(val1 & val2))
                elif instruction[1] == 'OR':
                    dict[instruction[4]] = np.uint16(int(val1 | val2))
                elif instruction[1] == 'LSHIFT':
                    dict[instruction[4]] = np.uint16(int(val1 << val2))
                elif instruction[1] == 'RSHIFT':
                    dict[instruction[4]] = np.uint16(int(val1 >> val2))
            elif instruction[0] == 'NOT':
                val1 = dict[instruction[1]]
                dict[instruction[3]] = np.uint16(int(~ val1))
        except:
            print('skipping', instruction)
            pass
        print('temp output:', dict)
    return dict


# print(part_a(data))



class Test(TestCase):
    def test_part_1_1(self):
        self.assertEqual(dict(d=72, e=507, f=492, g=114, h=65412, i=65079, x=123, y=456), part_a(
            ['123 -> in1', '456 -> in2', 'in1 AND in2 -> d', 'in1 OR in2 -> e', 'in1 LSHIFT 2 -> f', 'in2 RSHIFT 2 -> g', 'NOT in1 -> h',
             'NOT in2 -> i']))

    def test_part_1_2(self):
        self.assertEqual({'in1': 12, 'b': 13, 'a': 13} , part_a(
            ['12 -> in1','1 OR in1 -> b','b -> a']))