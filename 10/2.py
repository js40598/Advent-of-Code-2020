with open('input.txt') as file:
    tab = []
    tab.append(0)
    for line in file:
        tab.append(int(line.strip()))
    tab.append(max(tab) + 3)

tab.sort()


def generate_partitions(tab):
    partitions = [[]]
    for i in range(0, len(tab)):
        try:
            if tab[i] + 3 == tab[i+1]:
                partitions[-1].append(tab[i])
                partitions.append([])
            else:
                partitions[-1].append(tab[i])
        except IndexError:
            partitions[-1].append(tab[i])
    return partitions


def count_arrangements(partition):
    arrangements = []
    new_arrangements = [partition[0]]
    output = []
    while arrangements != new_arrangements:
        max_value = max(partition)
        arrangements = new_arrangements[::]
        new_arrangements = []
        for i in range(0, len(arrangements)):
            if arrangements[i] == max_value:
                output.append(arrangements[i])
            else:
                try:
                    if arrangements[i] + 1 in partition:
                        new_arrangements.append(arrangements[i] + 1)
                except IndexError:
                    if arrangements[i] + 1 in partition:
                        new_arrangements.append(arrangements[i] + 1)
                try:
                    if arrangements[i] + 2 in partition:
                        new_arrangements.append(arrangements[i] + 2)
                except IndexError:
                    if arrangements[i] + 2 in partition:
                        new_arrangements.append(arrangements[i] + 2)
                try:
                    if arrangements[i] + 3 in partition:
                        new_arrangements.append(arrangements[i] + 3)
                except IndexError:
                    if arrangements[i] + 3 in partition:
                        new_arrangements.append(arrangements[i] + 3)

        if not new_arrangements:
            new_arrangements = arrangements
    return len(output)


partitions = generate_partitions(tab)

outputs = []
for partition in partitions:
    outputs.append(count_arrangements(partition))


distinct_ways = 1

for o in outputs:
    distinct_ways = distinct_ways * o

print(distinct_ways)
