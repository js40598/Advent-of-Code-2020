from memory import get_memory_index, sum_values

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' = '))


def get_value(line):
    binary_value = bin(int(line[1]))[2::]
    binary_value = '0' * (36 - len(binary_value)) + binary_value
    result = ['0' for _ in range(0, 36)]
    for i in range(0, len(binary_value)):
        result[i] = binary_value[i] if mask[i] == 'X' else mask[i]
    return int(''.join(result), 2)


memory = {}
for line in tab:
    if line[0] == 'mask':
        mask = line[1]
    else:
        memory_index = get_memory_index(line)
        memory[memory_index] = get_value(line)

print(sum_values(memory))