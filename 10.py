from unittest import TestCase

input = '111221'


def iterate(input):
    output = []
    length = len(input)
    # print('length =', length)
    current_count = 1
    for current_index in range(0, length - 1):
        current_value = input[current_index]
        if input[current_index + 1] == current_value:
            # print('next index is the same. Value =', current_value)
            current_count += 1
        else:
            # print('there are', current_count, 'of the value', current_value)
            output.append(current_count)
            output.append(current_value)
            current_count = 1

        # last index handling
        if current_index == length - 2:
            if input[length - 1] != input[length - 2]:
                current_value = input[length - 1]
                # print('there are', 1, 'of the value', current_value)
                output.append(1)
                output.append(current_value)

    s = [str(i) for i in output]
    numout = str("".join(s))
    return numout


def iterate_n_times(input, times):
    for i in range(0, times):
        input = iterate(input)
        # print('interim after', i+1, 'step(s) =', input)
    return len(input)


val = iterate(input)
print(val)
print('part a:', iterate_n_times('1113222113', 40))
print('part b:', iterate_n_times('1113222113', 50))