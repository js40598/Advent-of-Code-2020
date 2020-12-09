with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(int(line.strip()))


for i in range(25, len(tab)):
    valid = False
    for j in range(i-25, i):
        for k in range(j, i):
            if tab[j] + tab[k] == tab[i] and tab[j] != tab[k]:
                valid = True
    if not valid:
        print(tab[i])
