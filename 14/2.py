import itertools
from memory import get_memory_index, sum_values

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' = '))


def use_mask(mask, memory_index):
    index_binary_value = bin(int(memory_index))[2::]
    index_binary_value = '0' * (36 - len(index_binary_value)) + index_binary_value
    result = ['0' for i in range(0, 36)]
    floats = 0
    for i in range(0, len(index_binary_value)):
        if mask[i] == 'X':
            floats += 1
            result[i] = 'X'
        elif mask[i] == '0':
            result[i] = index_binary_value[i]
        elif mask[i] == '1':
            result[i] = '1'
    return floats, result


def assign_combinations(floats, result, value):
    for i in itertools.product([0, 1], repeat=floats):
        current_result = []
        iter_counter = 0
        for j in result:
            if j == 'X':
                current_result.append(str(i[iter_counter]))
                iter_counter += 1
            else:
                current_result.append(j)
        memory[int(''.join(current_result), 2)] = value
    return memory


def get_value(line, memory):
    memory_index = get_memory_index(line)
    value = int(line[1])
    floats, result = use_mask(mask, memory_index)
    memory = assign_combinations(floats, result, value)
    return memory


memory = {}
for line in tab:
    if line[0] == 'mask':
        mask = line[1]
    else:
        memory = get_value(line, memory)

sum = sum_values(memory)
print(sum)
