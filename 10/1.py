with open('input.txt') as file:
    tab = []
    tab.append(0)
    for line in file:
        tab.append(int(line.strip()))
    tab.append(max(tab) + 3)

tab.sort()
for line in tab:
    print(line)

dictionary = {
    '1-jolt': 0,
    '3-jolt': 0,
}

print(tab)

for i in range(1, len(tab)):
    key = '{}-jolt'.format(tab[i] - tab[i-1])
    dictionary[key] += 1

print(dictionary)
print(dictionary['1-jolt'] * dictionary['3-jolt'])

# 10:54