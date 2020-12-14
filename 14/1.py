with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' = '))

memory = {}
for line in tab:
    if line[0] == 'mask':
        mask = line[1]
    else:
        memory_index = line[0][4:-1]
        binary_value = bin(int(line[1]))[2::]
        binary_value = '0' * (36 - len(binary_value)) + binary_value
        result = ['0' for i in range(0, 36)]
        for i in range(0, len(binary_value)):
            result[i] = binary_value[i] if mask[i] == 'X' else mask[i]
        memory[memory_index] = int(''.join(result), 2)
sum = 0
for key, value in memory.items():
    sum += value
print(sum)