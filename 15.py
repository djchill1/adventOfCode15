import re
from collections import Counter
import itertools

with open('15_input.txt') as fp:
    data = fp.read().splitlines()

with open('15_test.txt') as fp:
    testData = fp.read().splitlines()


def setup(data):
    cookieCapacity = 100
    names = []
    capacaties = []
    durabilities = []
    flavours = []
    textures = []
    calories = []
    for line in data:
        parsed = re.split(" ", line, 15)
        print(parsed)
        names.append(parsed[0].split(':')[0])
        capacaties.append(parsed[2].split(',')[0])
        durabilities.append(parsed[4].split(',')[0])
        flavours.append(parsed[6].split(',')[0])
        textures.append(parsed[8].split(',')[0])
        calories.append(parsed[10].split(',')[0])
    return names, capacaties, durabilities, flavours, textures, calories


def getScore(percs, capacaties, durabilities, flavours, textures, calories):
    max = len(percs)
    cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
    for i in range(0, max):
        # print('index', i)
        cap += percs[i] * int(capacaties[i])
        dur += percs[i] * int(durabilities[i])
        fla += percs[i] * int(flavours[i])
        tex += percs[i] * int(textures[i])
        cal += percs[i] * int(calories[i])
    if cap < 0:
        cap = 0
    elif dur < 0:
        dur = 0
    elif fla < 0:
        fla = 0
    # print(percs, cap, dur, fla, tex, cap * dur * fla * tex)
    return cap * dur * fla * tex, cal


def generate_weights(n):
    for t in itertools.combinations_with_replacement(range(100), n):
        if sum(t) == 100:
            yield from itertools.permutations(t)


# print(setup(testData))
# print(getScore([44, 56], ['-1', '2'], ['-2', '3'], ['6', '-2'], ['3', '-1']))


def getMax(data, calorieGoal=None):
    names, capacaties, durabilities, flavours, textures, calories = setup(data)
    numbOf = len(names)
    # print('numOf' ,numbOf, names)
    weights = generate_weights(numbOf)
    maxScore = 0
    for ratio in weights:
        # print('ratio is', ratio)
        score, cals = getScore(ratio, capacaties, durabilities, flavours, textures, calories)
        if score > maxScore:
            if calorieGoal is not None:
                if cals == calorieGoal:
                    maxScore = score
            else:
                maxScore = score
    return maxScore


print('max is', getMax(testData))
print('max is', getMax(data))
print('max is', getMax(data, 500))
