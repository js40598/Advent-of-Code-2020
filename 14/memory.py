def get_memory_index(line):
    return line[0][4:-1]


def sum_values(memory):
    sum = 0
    for key, value in memory.items():
        sum += value
    return sum