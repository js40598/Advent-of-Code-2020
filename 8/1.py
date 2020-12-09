with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' '))

for i in range(0, len(tab)):
    tab[i].append(False)

accumulator = 0
instruction = tab[0]
i = 0
first_loop = True
while first_loop:

    tab[i][2] = True

    if tab[i][0] == 'jmp':
        if tab[i][1][0] == '+':
            i += int(tab[i][1][1::])
        else:
            i += - int(tab[i][1][1::])
    elif tab[i][0] == 'acc':
        if tab[i][1][0] == '+':
            accumulator += int(tab[i][1][1::])
        else:
            accumulator += - int(tab[i][1][1::])
        i += 1
    elif tab[i][0] == 'nop':
        i += 1

    if tab[i][2]:
        print(accumulator)
        first_loop = False
