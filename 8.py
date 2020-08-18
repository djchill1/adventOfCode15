from unittest import TestCase

with open('8_input.txt') as fp:
    data = fp.read().splitlines()


def count_code_characters(input):
    return len(input)


def count_memory_characters(input):
    memory_char = eval(input)
    return len(memory_char)


def count_encoded_characters(input):
    return len(input) + input.count('"') + input.count('\\') + 2


def santas_list_length(data, part_a=True):
    output = 0
    for element in data:
        if part_a == True:
            output += count_code_characters(element)
            output -= count_memory_characters(element)
        else:
            output += count_encoded_characters(element)
            output -= count_code_characters(element)
    return output


print(santas_list_length(data, False))


class Test(TestCase):
    def test_part_1_1(self):
        with open('8_test.txt') as fp:
            data = fp.read().splitlines()

        self.assertEqual(12, santas_list_length(data))
