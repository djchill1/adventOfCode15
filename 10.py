from unittest import TestCase


def string_to_list(string):
    output = []
    for i in string:
        output.append(i)
    return output


def iterate(input):
    output = []
    length = len(input)
    for i in range(0, length):
        while input[i] == input[i+1]
        print(i)


iterate(['1', '2', '3', '4'])


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
