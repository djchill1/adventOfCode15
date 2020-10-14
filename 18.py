import numpy as np
import re

with open('18_input.txt') as fp:
    data = fp.read().splitlines()

with open('18_test.txt') as fp:
    testData = fp.read().splitlines()

# Part 1 - how many lights are on after 100 steps?
workingArr = []
for i in testData:
    parsed = re.split("", i, 100)
    parsed = list(filter(None, parsed))
    for index, i in enumerate(parsed):
        if i == '.':
            parsed[index] = 0
        else:
            parsed[index] = 1
    workingArr.append(parsed)
lightArr = np.array(workingArr)
print(lightArr)

def nextAnimation(inputMatrix):
    return np.count_nonzero(inputMatrix == 1)

print(nextAnimation(lightArr))