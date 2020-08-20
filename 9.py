from unittest import TestCase
from itertools import permutations


with open('9_input.txt') as fp:
    data = fp.read().splitlines()

def shortest_distance(data):
    places = set()
    distances = dict()
    for input_line in data:
        (source, _, dest, _, distance) = input_line.split()
        places.add(dest)
        places.add(source)
        distances.setdefault(source, dict())[dest] = int(distance)
        distances.setdefault(dest, dict())[source] = int(distance)
    print(distances)
    shortest = 99999999999999999999999999
    longest = 0
    for i in permutations(places):
        dist = sum(map(lambda x, y: distances[x][y], i[:-1], i[1:]))
        #print(dist)
        shortest = min(shortest, dist)
        longest = max(longest, dist)
    return shortest, longest

print(shortest_distance(data))

class Test(TestCase):
    def test_part_1_1(self):
        with open('9_test.txt') as fp:
            data = fp.read().splitlines()

        self.assertEqual(605, shortest_distance(data))
