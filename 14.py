from unittest import TestCase
import re
from collections import Counter

with open('14_input.txt') as fp:
    data = fp.read().splitlines()

with open('14_test.txt') as fp:
    testData = fp.read().splitlines()


def split_input(data):
    instructions = []
    for instruction in data:
        parsed = re.split(" ", instruction, 15)
        parsedDict = {'name': parsed[0], 'speed': parsed[3], 'duration': parsed[6], 'rest': parsed[13]}
        instructions.append(parsedDict)
    return instructions


def get_winner(input, duration):
    inputList = split_input(input)
    distances = []
    for reindeer in inputList:
        reindeerName = reindeer['name']
        speed = int(reindeer['speed'])
        travel = int(reindeer['duration'])
        rest = int(reindeer['rest'])
        time = duration
        q, r = divmod(time, travel + rest)
        totalDistance = (q * travel + min(r, travel)) * speed
        distances.append({'name': reindeerName, 'distance': totalDistance})
    return sorted(distances, key=lambda i: i['distance'], reverse=True)

# print(get_winner(data, 2503))
# print(get_winner(testData, 1000))


def calculate_score(input, time):
    winnersList = []
    for t in range(1, time + 1):
        winners = get_winner(input, t)
        # print(len(winners))
        # print(winners)
        winnersList.append(winners[0]['name'])
        for i in range(0, len(winners) - 1):
            if winners[0]['distance'] == winners[i + 1]['distance']:
                # print('equal')
                winnersList.append(winners[i+1]['name'])
    scores = Counter(winnersList)
    print(scores)


calculate_score(data, 2503)

