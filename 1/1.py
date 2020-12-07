tab = []

with open('input.txt') as file:
    for line in file:
        tab.append(int(line.strip()))


def find_pair(tab, value):
    for i in range(0, len(tab)):
        for j in range(i, len(tab)):
            if tab[i] + tab[j] == 2020:
                return tab[i] * tab[j]


print(find_pair(tab, 2020))
