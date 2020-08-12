from unittest import TestCase


def password_to_list(string):
    output = []
    for i in string:
        output.append(i)
    return output


def first_requirement(password):
    # one increasing straight of at least three letters like abc, bcd, cde.
    return False


def second_requirement(password):
    # may not contain the letters i, o, or l.
    bad_characters = ['i', 'o', 'l']
    intersection = set(password).intersection(set(bad_characters))
    if len(intersection) == 0:
        return True
    else:
        return False


def third_requirement(password):
    # must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz
    return False



def part_a(string):
    password = password_to_list(string)


print(password_to_list('hijklmmn'))


class Test(TestCase):
    def test_part_1_1(self):
        self.assertEqual(False, part_a('hijklmmn'))

    def test_part_1_2(self):
        self.assertEqual(False, part_a('abbceffg'))

    def test_part_1_3(self):
        self.assertEqual(False, part_a('abbcegjk'))

    # def test_part_2_1(self):
    #     self.assertEqual(1, part_b(['turn on 0,0 through 0,0']))
    #
    # def test_part_2_2(self):
    #     self.assertEqual(2000000, part_b(['toggle 0,0 through 999,999']))
    #
    # def test_part_2_3(self):
    #     self.assertEqual(False, is_nice_2('uurcxstgmygtbstg'))
    #
    # def test_part_2_4(self):
    #     self.assertEqual(False, is_nice_2('ieodomkazucvgmuy'))
    #
    # def test_part_2_5(self):
    #     self.assertEqual(False, is_nice_2('aaa'))
