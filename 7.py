import init, re

data = init.read_data(False, )


def circuit_calculator(rule, values):
    unsupported = False
    parsed = re.split(" ", rule, 6)
    # print(parsed)
    if parsed[1] == '->':
        if parsed[0] in values:
            values[parsed[2]] = values[parsed[0]]
        elif parsed[0] .isnumeric():
            values[parsed[2]] = int(parsed[0])
    elif parsed[1] in ('AND', 'OR'):
        # print(parsed)
        if parsed[0].isnumeric() and parsed[2] in values:
            in1 = int(parsed[0])
            in2 = values[parsed[2]]
        elif parsed[0] in values and parsed[2] in values:
            in1 = values[parsed[0]]
            in2 = values[parsed[2]]
        else:
            return values, True
        and_or_gates = {
            'AND': in1 & in2,
            'OR': in1 | in2,
            'NOT': ~ in1
        }
        output = and_or_gates[parsed[1]]
        values[parsed[4]] = output
    elif parsed[1] in ('LSHIFT', 'RSHIFT') and parsed[0] in values:
        in1 = values[parsed[0]]
        in2 = int(parsed[2])
        l_r_shift_gates = {
            'LSHIFT': in1 << in2,
            'RSHIFT': in1 >> in2
        }
        output = l_r_shift_gates[parsed[1]]
        # print('shifts', in1, in2, output, l_r_shift_gates)
        values[parsed[4]] = output
    elif parsed[0] == 'NOT' and parsed[1] in values:
        in1 = values[parsed[1]]
        output = (~ in1)%65535 + 1
        values[parsed[3]] = output
    else:
        unsupported = True
        # print('unsuported character', parsed)
    # print(values)
    return values, unsupported


def part1_iter(data, values, partb=False):
    unsupported_count = 0
    for rule in data:
        values, unsupported = circuit_calculator(rule, values)
        if partb:
            values['b'] = 956
        if unsupported:
            unsupported_count += 1
    return values, unsupported_count


def part1(data):
    values = {}
    unsupported_count = 1
    while unsupported_count != 0:
        values, unsupported_count = part1_iter(data, values)
        print(unsupported_count, values)
    return values['a']

def part2(data):
    print('***** PART 2 ******')
    values = {'b': 956}
    unsupported_count = 1
    while unsupported_count != 0:
        values, unsupported_count = part1_iter(data, values, True)
        # values['b'] = 956
        print(unsupported_count, values)
    return values['a']


print(f'Part 1: {part1(data)}, Part 2: {part2(data)}')