def prepare_data(tab):
    if len(tab[0]) == 2:
        for i in range(0, len(tab)):
            tab[i].append(False)
    else:
        for i in range(0, len(tab)):
            tab[i][-1] = False
    return tab


def loop(tab):
    accumulator = 0
    i = 0
    while not tab[i][2]:
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
        try:
            if tab[i][2]:
                return accumulator
        except IndexError:
            return accumulator, True
