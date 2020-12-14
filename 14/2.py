import itertools

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
        value = int(line[1])
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
sum = 0
for key, value in memory.items():
    sum += value
print(sum)