from unittest import TestCase

with open('2_input.txt') as fp:
    data = fp.read().splitlines()


def paper_per_present(dimensions):
    l, w, h = dimensions.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    area = [l * w, w * h, h * l]
    return 2 * sum(area) + min(area)


def total_paper(dimensionsList):
    paper = 0
    for present in dimensionsList:
        paper += paper_per_present(present)
    return paper


print('part 1', total_paper(data))


def ribbon_per_present(dimensions):
    l, w, h = dimensions.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    perimeters = [2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h]
    volume = l * w * h
    return min(perimeters) + volume


def total_ribbon(dimensionsList):
    ribbon = 0
    for present in dimensionsList:
        ribbon += ribbon_per_present(present)
    return ribbon


print('part 2', total_ribbon(data))


class Test(TestCase):

    def test_part_1_1(self):
        self.assertEqual(58, paper_per_present('2x3x4'))

    def test_part_1_2(self):
        self.assertEqual(43, paper_per_present('1x1x10'))

    def test_part_2_1(self):
        self.assertEqual(34, ribbon_per_present('2x3x4'))

    def test_part_2_2(self):
        self.assertEqual(14, ribbon_per_present('1x1x10'))
