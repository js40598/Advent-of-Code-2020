with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(int(line.strip()))
    for i in range(0, len(tab)):
        for j in range(i, len(tab)):
            if tab[i] + tab[j] == 2020:
                print(tab[i] * tab[j])
