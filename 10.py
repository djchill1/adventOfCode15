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
        temp_sum = 0
        print('parsing', i, input[i])
        try:
            if input[i] == input[i+1]:
                print(input[i], 'equal!')
                temp_sum += 1
        except:
            pass


def part_a_result(number):
    return iterate(string_to_list(number))


def part_a(start_number, iterations):
    result = 0
    return len(result)


iterate(['1', '2', '2', '4'])


class Test(TestCase):
    def test_part_1_1(self):
        self.assertEqual(11, part_a_result(1))

    def test_part_1_2(self):
        self.assertEqual(21, part_a_result(11))

    def test_part_1_3(self):
        self.assertEqual(1211, part_a_result(21))

    def test_part_1_4(self):
        self.assertEqual(111221, part_a_result(1211))

    def test_part_1_5(self):
        self.assertEqual(312211, part_a_result(111221))