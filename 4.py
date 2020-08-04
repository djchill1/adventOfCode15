from unittest import TestCase
import hashlib

# TODO: Actually make this work, it really doesn't atm!

data = 'ckczppom'

m = hashlib.md5()
m.update(("abcdef"+str(609043)).encode('utf-8'))
hex = m.hexdigest()
print(hex)

def part_a(input):
    hex = '11111111111'
    num = 1000
    while hex[:5] != '00000':
        num += 1
        m.update(("abcdef"+str(num)).encode('utf-8'))
        hex = m.hexdigest()
    return num


class Test(TestCase):
    def test_part_1_1(self):
        self.assertEqual(609043, part_a('abcdef'))

    def test_part_1_2(self):
        self.assertEqual(1048970, part_a('pqrstuv'))
