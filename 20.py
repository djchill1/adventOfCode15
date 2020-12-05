import math
import numpy as np


def get_presents_list(elf_number, max_houses):
    presents_list = []
    for index in range(1, max_houses):
        if index % elf_number == 0:
            presents = elf_number * 10
        else:
            presents = 0
        # print(index, presents)
        presents_list.append(presents)
    return presents_list


maximum = 60000
presents_sum = np.zeros(maximum - 1)

for elf in range(1, maximum):
    print('elf', elf)
    elf_presents = get_presents_list(elf, maximum)
    # print(elf_presents)
    presents_sum = np.add(presents_sum, elf_presents)

print(presents_sum)

for i in presents_sum:
    if i >= 29000000:
        print(i)
        break

print(presents_sum[500])