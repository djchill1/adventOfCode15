import re

with open('16_sues.txt') as fp:
    sues_data = fp.read().splitlines()


def setup(data):
    sueInfo = []
    for line in data:
        tempSue = []
        parsed = re.split(" ", line, 15)
        # print(parsed)
        tempSue.append(parsed[1].split(':')[0])
        tempSue.append(parsed[2].split(':')[0])
        tempSue.append(int(parsed[3].split(',')[0]))
        tempSue.append(parsed[4].split(':')[0])
        tempSue.append(int(parsed[5].split(',')[0]))
        tempSue.append(parsed[6].split(':')[0])
        tempSue.append(int(parsed[7].split(',')[0]))
        sueInfo.append(tempSue)
    return sueInfo


sueDict = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
           'trees': 3, 'cars': 2, 'perfumes': 1}

print(sueDict['children'])
print(setup(sues_data))


def matchesDict(item, value, dicto, part2=False):
    greaterThans = ['cats', 'trees']
    lessThans = ['pomeranians', 'goldfish']
    equalTos = ['children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes']
    if item in dicto:
        if part2 == True:
            if item in greaterThans:
                if value > dicto[item]:
                    return True
            elif item in lessThans:
                if value < dicto[item]:
                    return True
            else:
                if value == dicto[item]:
                    return True
        else:
            if value == dicto[item]:
                return True
    return False


for line in setup(sues_data):
    trueCount = 0
    for i in range(1, 6, 2):
        if matchesDict(line[i], line[i + 1], sueDict) == True:
            trueCount += 1
    if trueCount == 3:
        print('sue', line[0])

for line in setup(sues_data):
    trueCount = 0
    for i in range(1, 6, 2):
        if matchesDict(line[i], line[i + 1], sueDict, True) == True:
            trueCount += 1
    if trueCount == 3:
        print('sue', line[0])