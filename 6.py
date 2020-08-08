from unittest import TestCase
import numpy as np
import re

with open('6_input.txt') as fp:
    data = fp.read().splitlines()


def split_input(data):
    instructions = []
    for instruction in data:
        parsed = re.split(" |,", instruction, 8)
        if parsed[0] == 'turn':
            parsed.remove('turn')
        parsed.remove('through')
        instructions.append(parsed)
    return instructions


def parse_instructions(instructions, part_a=True):
    lights = np.zeros((1000, 1000))
    for input in instructions:
        x0, y0, x1, y1 = input[1:]
        x0 = int(x0)
        x1 = int(x1)
        y0 = int(y0)
        y1 = int(y1)
        # print(x0,x1,y0,y1, input[0])
        if part_a:
            if input[0] == 'toggle':
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        lights[x][y] = 1 - lights[x][y]
            elif input[0] == 'on':
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        lights[x][y] = 1
            elif input[0] == 'off':
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        lights[x][y] = 0
            else:
                print('Could not parse:', input)
        else:
            if input[0] == 'toggle':
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        lights[x][y] += 2
            elif input[0] == 'on':
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        lights[x][y] += 1
            elif input[0] == 'off':
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        lights[x][y] -= 1
                        if lights[x][y] < 0:
                            lights[x][y] = 0
            else:
                print('Could not parse:', input)

    return lights


def lights_on(array):
    return sum(sum(array))


def part_a(list):
    return lights_on(parse_instructions(split_input(list)))


def part_b(list):
    return lights_on(parse_instructions(split_input(list), False))


print('a', part_a(data))
print('b', part_b(data))


class Test(TestCase):
    def test_part_1_1(self):
        self.assertEqual(1000000, part_a(['turn on 0,0 through 999,999']))

    def test_part_1_2(self):
        self.assertEqual(1000, part_a(['toggle 0,0 through 999,0']))

    def test_part_1_3(self):
        self.assertEqual(0, part_a(['turn off 499,499 through 500,500']))

    def test_part_2_1(self):
        self.assertEqual(1, part_b(['turn on 0,0 through 0,0']))

    def test_part_2_2(self):
        self.assertEqual(2000000, part_b(['toggle 0,0 through 999,999']))
    #
    # def test_part_2_3(self):
    #     self.assertEqual(False, is_nice_2('uurcxstgmygtbstg'))
    #
    # def test_part_2_4(self):
    #     self.assertEqual(False, is_nice_2('ieodomkazucvgmuy'))
    #
    # def test_part_2_5(self):
    #     self.assertEqual(False, is_nice_2('aaa'))
