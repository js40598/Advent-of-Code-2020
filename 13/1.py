with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(','))

counter = 0
while 'x' in tab[1]:
    if tab[1][counter] == 'x':
        tab[1].pop(counter)
    else:
        counter += 1

tab[0] = int(tab[0][0])
departs = []
for i in range(0, len(tab[1])):
    departs.append((int(tab[0] / int(tab[1][i])) + 1) * int(tab[1][i]))
print(int(tab[1][departs.index(min(departs))]) * (min(departs) - tab[0]))

