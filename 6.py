from unittest import TestCase
import numpy as np
import re

with open('6_input.txt') as fp:
    data = fp.read().splitlines()


instructions = []

for instruction in data:
    parsed = re.split(" |,", instruction, 8)
    if parsed[0] == 'turn':
        parsed.remove('turn')
    parsed.remove('through')
    instructions.append(parsed)


def parse_instructions(instructions):
    lights = np.zeros((1000, 1000))
    for input in instructions:
        x0, y0, x1, y1 = input[1:]
        x0 = int(x0)
        x1 = int(x1)
        y0 = int(y0)
        y1 = int(y1)
        if input[0] == 'toggle':
            for x in range(x0, x1):
                for y in range(y0, y1):
                    lights[x][y] = 1 - lights[x][y]
        elif input[0] == 'on':
            for x in range(x0, x1):
                for y in range(y0, y1):
                    lights[x][y] = 1
        elif input[0] == 'off':
            for x in range(x0, x1):
                for y in range(y0, y1):
                    lights[x][y] = 0
        else:
            print('Could not parse:', input)
    return lights


def lights_on(array):
    return np.sum(array)


print(lights_on(parse_instructions(instructions)))




# class Test(TestCase):
    # def test_part_1_1(self):
    #     self.assertEqual(True, is_nice('turn on 0,0 through 999,999'))
    #
    # def test_part_1_2(self):
    #     self.assertEqual(True, is_nice('toggle 0,0 through 999,0'))
    #
    # def test_part_1_3(self):
    #     self.assertEqual(False, is_nice('turn off 499,499 through 500,500'))

    # def test_part_2_1(self):
    #     self.assertEqual(True, is_nice_2('qjhvhtzxzqqjkmpb'))
    #
    # def test_part_2_2(self):
    #     self.assertEqual(True, is_nice_2('xxyxx'))
    #
    # def test_part_2_3(self):
    #     self.assertEqual(False, is_nice_2('uurcxstgmygtbstg'))
    #
    # def test_part_2_4(self):
    #     self.assertEqual(False, is_nice_2('ieodomkazucvgmuy'))
    #
    # def test_part_2_5(self):
    #     self.assertEqual(False, is_nice_2('aaa'))