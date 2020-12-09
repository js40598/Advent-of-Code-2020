from loops import prepare_data, loop

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' '))


def change_operation(operation):
    if operation == 'jmp':
        return 'nop'
    elif operation == 'nop':
        return 'jmp'


tab = prepare_data(tab)

for i in range(0, len(tab)):
    if tab[i][0] in 'jmp nop':
        tab[i][0] = change_operation(tab[i][0])

        output = loop(tab)
        if not isinstance(output, int):
            print(output[0])

        tab = prepare_data(tab)
        tab[i][0] = change_operation(tab[i][0])
