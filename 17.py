import itertools
import math

with open('17_input.txt') as fp:
    data = fp.read().splitlines()

containersInts = []
for i in data:
    containersInts.append(int(i))


def generate_permutations(containers, total):
    for i in range(len(containers)):
        for t in itertools.combinations(containers, i):
            if sum(t) == total:
                yield from itertools.permutations(t)


perms = generate_permutations(containersInts, 150)
lengths = []
counts = []
for perm in perms:
    lengths.append(len(perm))
    # print(sorted(perm))
for i in range(len(lengths)):
    # print(i, 'count', int(lengths.count(i)/math.factorial(i)))
    counts.append(int(lengths.count(i)/math.factorial(i)))
print(sum(counts))

# containersInts = [20, 15, 10, 5, 5]
# perms = generate_permutations(containersInts, 25)
# lengths = []
# counts = []
# for perm in perms:
#     lengths.append(len(perm))
#     print(sorted(perm))
# for i in range(len(lengths)):
#     print(i, 'count', int(lengths.count(i)/math.factorial(i)))
#     counts.append(int(lengths.count(i)/math.factorial(i)))
# print(sum(counts))


