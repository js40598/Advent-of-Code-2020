with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' '))

for row in range(0, len(tab)):
    tab[row].append(False)

for i in range(0, len(tab)):
    changed = False
    if tab[i][0] == 'jmp':
        tab[i][0] = 'nop'
        changed = True
    elif tab[i][0] == 'nop':
        tab[i][0] = 'jmp'
        changed = True

    for j in range(0, len(tab)):
        tab[j][-1] = False

    if changed:
        accumulator = 0
        instruction = tab[0]
        row = 0
        first_loop = True
        while first_loop:

            tab[row][2] = True

            if tab[row][0] == 'jmp':
                if tab[row][1][0] == '+':
                    row += int(tab[row][1][1::])
                else:
                    row += - int(tab[row][1][1::])
            elif tab[row][0] == 'acc':
                if tab[row][1][0] == '+':
                    accumulator += int(tab[row][1][1::])
                else:
                    accumulator += - int(tab[row][1][1::])
                row += 1
            elif tab[row][0] == 'nop':
                row += 1

            try:
                if tab[row][2]:
                    first_loop = False
            except IndexError:
                print(accumulator)
                first_loop = False

        if tab[i][0] == 'jmp':
            tab[i][0] = 'nop'
        elif tab[i][0] == 'nop':
            tab[i][0] = 'jmp'
