with open('input.txt') as file:
    tab = []
    tab.append(0)
    for line in file:
        tab.append(int(line.strip()))
    tab.append(max(tab) + 3)

tab.sort()

dictionary = {
    '1-jolt': 0,
    '3-jolt': 0,
}

for i in range(1, len(tab)):
    try:
        key = '{}-jolt'.format(tab[i] - tab[i-1])
        dictionary[key] += 1
    except KeyError:
        pass

print(dictionary)
print(dictionary['1-jolt'] * dictionary['3-jolt'])
