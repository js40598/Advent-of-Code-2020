with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip().split(' contain '))

for i in range(0, len(tab)):
    tab[i][0] = tab[i][0].split(' ')
    tab[i][0].pop()
    tab[i][0] = ' '.join(tab[i][0])

for i in range(0, len(tab)):
    tab[i][1] = tab[i][1].split(', ')
    for j in range(0, len(tab[i][1])):

        tab[i][1][j] = tab[i][1][j].split(' ')
        tab[i][1][j].pop()
        tab[i][1][j] = [tab[i][1][j][0], ' '.join(tab[i][1][j][1::])]

for b in tab:
    if b[0] in 'drab fuchsia mirrored purple dotted green':
        print(b)


def required_bags(pattern, tab):
    output = 0
    for i in range(0, len(tab)):
        if tab[i][0] == pattern:
            for j in range(0, len(tab[i][1])):
                try:
                    output += int(tab[i][1][j][0])
                    rec = required_bags(tab[i][1][j][1], tab)
                    output += (int(tab[i][1][j][0]) * rec) if rec != '0' else 0
                except ValueError:
                    pass
    return output


print(required_bags('shiny gold', tab))

