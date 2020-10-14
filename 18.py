import numpy as np
import re
import itertools

with open('18_input.txt') as fp:
    data = fp.read().splitlines()

with open('18_test.txt') as fp:
    testData = fp.read().splitlines()

# Part 1 - how many lights are on after 100 steps?
workingArr = []
for i in data:
    parsed = re.split("", i, 100)
    parsed = list(filter(None, parsed))
    for index, i in enumerate(parsed):
        if i == '.':
            parsed[index] = 0
        else:
            parsed[index] = 1
    workingArr.append(parsed)
lightArr = np.array(workingArr)

# part 2 - lights stuck on:

lightArr[0, 0] = 1
lightArr[0, len(lightArr) - 1] = 1
lightArr[len(lightArr) - 1, 0] = 1
lightArr[len(lightArr) - 1, len(lightArr) - 1] = 1

print(lightArr)


def checkNeighbours(initRowVal, initColVal, lightArr, debug=False):
    countOn = 0
    for row in range(initRowVal - 1, initRowVal + 2):
        for col in range(initColVal - 1, initColVal + 2):
            if row in range(0, len(lightArr)):
                if col in range(0, len(lightArr[0])):
                    if col - initColVal == 0 and row - initRowVal == 0:
                        if debug:
                            print(row, col, 'same value as start index')
                        pass
                    else:
                        if debug:
                            print(row, col, 'light has value', lightArr[row, col])
                        countOn += lightArr[row, col]
                else:
                    if debug:
                        print(row, col, 'out of col count')
                    pass
            else:
                if debug:
                    print(row, col, 'out of row count')
                pass
    return countOn


def nextAnimation(inputMatrix, debug=False, lightsStuckOn=False):
    nextView = np.zeros((len(inputMatrix), len(inputMatrix)), dtype=int)
    for rowVal, rowvals in enumerate(inputMatrix):
        for colVal, indVal in enumerate(rowvals):
            currentVal = inputMatrix[rowVal, colVal]
            neighboursOn = checkNeighbours(rowVal, colVal, inputMatrix)
            if debug:
                print('(', rowVal, ',', colVal, ') =', currentVal, 'number of neighbours on', neighboursOn)
            if currentVal == 0 and neighboursOn == 3:
                # should be turning on if there are 3 neighbours on
                nextView[rowVal, colVal] = 1
                if debug:
                    print('setting', rowVal, colVal, 'to 1 from 0')
            if currentVal == 1 and neighboursOn in (2, 3):
                # should be staying on if 2 or 3 neighbours are on
                nextView[rowVal, colVal] = 1
                if debug:
                    print('setting', rowVal, colVal, 'to 1 from 1')
            if lightsStuckOn:
                nextView[0, 0] = 1
                nextView[0, len(nextView) - 1] = 1
                nextView[len(nextView) - 1, 0] = 1
                nextView[len(nextView) - 1, len(nextView) - 1] = 1
    return nextView


# print('countOn', checkNeighbours(0, 2, lightArr, True))
view = lightArr
for i in range(1, 101):
    print('after', i, 'steps:')
    view = nextAnimation(view, False, True)
    print(view)
    print(np.sum(view))
# print(lightArr[0,1])
# print(lightArr)
