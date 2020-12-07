tab = []

with open('input.txt') as file:
    for line in file:
        tab.append(int(line.strip()))


def find_three(tab, value):
    for i in range(0, len(tab)):
        for j in range(i, len(tab)):
            for k in range(j, len(tab)):
                if tab[i] + tab[j] + tab[k] == 2020:
                    return tab[i] * tab[j] * tab[k]


print(find_three(tab, 2020))
