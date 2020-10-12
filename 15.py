import re
from collections import Counter
import itertools

with open('15_input.txt') as fp:
    data = fp.read().splitlines()

with open('15_test.txt') as fp:
    testData = fp.read().splitlines()

cookieCapacity = 100
names = []
capacaties = []
durabilities = []
flavours = []
textures = []

def setup(data):
    for line in data:
        parsed = re.split(" ", line, 15)
        print(parsed)
        names.append(parsed[0].split(':')[0])
        capacaties.append(parsed[2].split(',')[0])
        durabilities.append(parsed[4].split(',')[0])
        flavours.append(parsed[6].split(',')[0])
        textures.append(parsed[8].split(',')[0])
    return names, capacaties, durabilities, flavours, textures

def getScore():




print(setup(testData))