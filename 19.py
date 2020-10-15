import re

startString = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
startString = 'H2O'

with open('19_input.txt') as fp:
    data = fp.read().splitlines()

with open('19_test.txt') as fp:
    testdata = fp.read().splitlines()

keys = []
replacements = []
for i in testdata:
    parsed = re.split(" ", i, 3)
    parsed = list(filter(None, parsed))
    keys.append(parsed[0])
    replacements.append(parsed[2])
print(keys, replacements)

outLists = []

for i in range(0, len(startString)):
    currentValue = startString[i]
    print('checking value', currentValue)
    for index, key in enumerate(keys):
        if key == currentValue:
            # print(key, 'is current key')
            outString = startString[:i] + replacements[index] + startString[i + 1:]
            if outString not in outLists:
                outLists.append(outString)
                print('outputted string', outString)

# When there are 2 character keys
for i in range(0, len(startString) - 1):
    currentValue = startString[i:i + 2]
    print('checking value', currentValue)
    for index, key in enumerate(keys):
        if key == currentValue:
            # print(key, 'is current key')
            outString = startString[:i] + replacements[index] + startString[i + 1:]
            if outString not in outLists:
                outLists.append(outString)
                print('outputted string', outString)

print('## OUTPUT ## number of values', len(outLists))
