from loops import loop, prepare_data

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' '))

tab = prepare_data(tab)

print(loop(tab))
