import itertools

with open('17_input.txt') as fp:
    data = fp.read().splitlines()

containersInts = []
for i in data:
    containersInts.append(int(i))

# Part 1 - Sum the number of all combinations that hold 150 L.
total = 0
for i in range(1, len(containersInts) + 1):
    total += len([x for x in itertools.combinations(containersInts, i) if sum(x) == 150])
print(total)

# Part 2 - Break after the smallest number
total = 0
for i in range(1, len(containersInts) + 1):
    total += len([x for x in itertools.combinations(containersInts, i) if sum(x) == 150])
    if total > 0:
        break
print(total)
