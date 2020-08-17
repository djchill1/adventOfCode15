from unittest import TestCase
import hashlib


def part_a(key, zeros=5):
    i = 0
    n_zero_index = 0
    while True:
        i += 1
        hash = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()

        if not n_zero_index and hash.startswith('0' * zeros):
            n_zero_index = i

        # exit
        if (n_zero_index):
            break

    return i, hash


print(part_a('ckczppom'))
print(part_a('ckczppom', 6))


class Test(TestCase):
    def test_part_1_1(self):
        self.assertEqual(609043, part_a('abcdef')[0])

    def test_part_1_2(self):
        self.assertEqual(1048970, part_a('pqrstuv')[0])
