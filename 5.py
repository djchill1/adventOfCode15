from unittest import TestCase

with open('5_input.txt') as fp:
    data = fp.read().splitlines()


def part_a(list):
    count = 0
    for string in list:
        if is_nice(string) == True:
            count += 1
    return count

def part_b(list):
    count = 0
    for string in list:
        if is_nice_2(string) == True:
            count += 1
    return count


def is_nice(string):
    print('vowels', contains_at_least_3_vowels(string))
    print('twice', letter_twice_in_a_row(string))
    print('not', not_specific_strings(string))
    if contains_at_least_3_vowels(string) == True and letter_twice_in_a_row(string) == True and not_specific_strings(
            string) is None:
        return True
    else:
        return False


def contains_at_least_3_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for letter in string:
        if letter in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        return True
    else:
        return False


def letter_twice_in_a_row(string):
    twices = 0
    for index in range(1, len(string)):
        if string[index - 1] == string[index]:
            twices += 1
    if twices > 0:
        return True
    else:
        return False


def not_specific_strings(string):
    exclusions = ['ab', 'cd', 'pq', 'xy']
    for exclusion in exclusions:
        if exclusion in string:
            return False


def is_nice_2(string):
    print('overlap', non_overlapping_pairs(string))
    print('repeats', repeats_with_between(string))
    if non_overlapping_pairs(string) == True and repeats_with_between(string) == True:
        return True
    else:
        return False


def non_overlapping_pairs(string):
    pairs = 0
    for index in range(2, len(string)):
        pair = string[index - 2:index]
        string_minus_pair = string[index:]
        # print('pair', pair)
        # print('string', string_minus_pair)
        if pair in string_minus_pair:
            pairs += 1
    if pairs > 0:
        return True
    else:
        return False


def repeats_with_between(string):
    twices = 0
    for index in range(2, len(string)):
        if string[index - 2] == string[index]:
            twices += 1
    if twices > 0:
        return True
    else:
        return False


print(part_a(data))
print(part_b(data))


class Test(TestCase):

    def test_part_1_1(self):
        self.assertEqual(True, is_nice('ugknbfddgicrmopn'))

    def test_part_1_2(self):
        self.assertEqual(True, is_nice('aaa'))

    def test_part_1_3(self):
        self.assertEqual(False, is_nice('jchzalrnumimnmhp'))

    def test_part_1_4(self):
        self.assertEqual(False, is_nice('haegwjzuvuyypxyu'))

    def test_part_1_5(self):
        self.assertEqual(False, is_nice('dvszwmarrgswjxmb'))

    def test_part_2_1(self):
        self.assertEqual(True, is_nice_2('qjhvhtzxzqqjkmpb'))

    def test_part_2_2(self):
        self.assertEqual(True, is_nice_2('xxyxx'))

    def test_part_2_3(self):
        self.assertEqual(False, is_nice_2('uurcxstgmygtbstg'))

    def test_part_2_4(self):
        self.assertEqual(False, is_nice_2('ieodomkazucvgmuy'))

    def test_part_2_5(self):
        self.assertEqual(False, is_nice_2('aaa'))