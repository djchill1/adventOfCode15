import init, re

data = init.read_data(True, )

for rule in data:
    print(rule)


def part1(data):
	values = {}
	in1 = 0
	in2 = 0
	gates = {
		'AND': in1 & in2,
		'OR': in1 | in2,
		'LSHIFT': in1 << in2,
		'RSHIFT': in1 >> in2,
		'NOT': ~ in1
	}
	for rule in data:
		parsed = re.split(" ", rule, 6)
		print(parsed)
	return False


def part2():
    return False


print(f'Part 1: {part1(data)}, Part 2: {part2(data)}')
