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
    for instruction in parsed:
        # print(instruction)
        try:
            if instruction[1] == '->':
                print(instruction[2], instruction[0])
                dict[instruction[2]] = np.uint16(int(instruction[0]))
            elif instruction[1] == 'AND':
                val1 = dict[instruction[0]]
                val2 = dict[instruction[2]]
                dict[instruction[4]] = np.uint16(int(val1 & val2))
            elif instruction[1] == 'OR':
                val1 = dict[instruction[0]]
                val2 = dict[instruction[2]]
                dict[instruction[4]] = np.uint16(int(val1 | val2))
            elif instruction[1] == 'LSHIFT':
                val1 = dict[instruction[0]]
                val2 = int(instruction[2])
                dict[instruction[4]] = np.uint16(int(val1 << val2))
            elif instruction[1] == 'RSHIFT':
                val1 = dict[instruction[0]]
                val2 = int(instruction[2])
                dict[instruction[4]] = np.uint16(int(val1 >> val2))
            elif instruction[0] == 'NOT':
                val1 = dict[instruction[1]]
                dict[instruction[3]] = np.uint16(int(~ val1))
        except:
            pass
    return dict


# print(part_a(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h',
#               'NOT y -> i']))

# print(part_a(data))


# a = dict(d=72, e=507, f=492, g=114, h=65412, i=65079, x=123, y=456)
# a['d'] = 1
#
# print(a)

class Test(TestCase):
    # def test_part_1_1(self):
    #     self.assertEqual(dict(d=72, e=507, f=492, g=114, h=65412, i=65079, x=123, y=456), part_a(
    #         ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h',
    #          'NOT y -> i']))

    def test_part_1_2(self):
        self.assertEqual(13, part_a(
            ['12 -> x','1 OR x -> b','b -> a']))