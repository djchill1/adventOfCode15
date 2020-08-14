from unittest import TestCase


def password_to_list(string):
    output = []
    for i in string:
        output.append(i)
    return output


def list_to_string(pw_list):
    string = ''
    for element in pw_list:
        string += element
    return string


def first_requirement(password):
    # one increasing straight of at least three letters like abc, bcd, cde.
    for index in range(0, len(password) - 2):
        if ord(password[index]) + 1 == ord(password[index + 1]):
            if ord(password[index + 1]) + 1 == ord(password[index + 2]):
                return True
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
    pairs = 0
    for index in range(0, len(password) - 1):
        if password[index] == password[index + 1]:
            try:
                if password[index] != password[index + 2]:
                    pairs += 1
            except:
                pairs += 1
    if pairs >= 2:
        return True
    else:
        return False


def next_password(chars_list, password_length=8):
    # FYIs:
    # ord(a) = 97
    # ord(z) = 122
    ords = []
    for i in range(0, password_length):
        ords.append(0)
    index = 0
    next_pass = []
    for char in chars_list:
        ords[index] = ord(char)
        index += 1
    ords[password_length - 1] += 1
    index = password_length - 1
    for char in reversed(ords):
        if char > 122:
            if index > 0:
                # print(index)
                # print(ords)
                # print(char, ords[index], ords[index-1])
                ords[index] = 97
                ords[index-1] += 1
            else:
                print('PW OUT OF RANGE FOR LOOP')
        index -= 1

    for element in ords:
        next_pass.append(chr(element))
    return next_pass


def part_a(starting_string):
    string = starting_string
    password = password_to_list(string)
    r1, r2, r3 = False, False, False
    while r1 is False or r2 is False or r3 is False:
        password = next_password(password)
        print('working pw', password)
        r1 = first_requirement(password)
        r2 = second_requirement(password)
        r3 = third_requirement(password)
        print(r1, r2, r3)
    return list_to_string(password)


print(part_a('cqjxxyzz'))
# print(part_a('ghijklmn'))


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
