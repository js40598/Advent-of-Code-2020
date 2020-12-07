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


def search_possible_bags(pattern, tab):
    output = set()
    for i in range(0, len(tab)):
        for j in range(0, len(tab[i][1])):
            if tab[i][1][j][1] == pattern:
                output.add(tab[i][0])
                rec = search_possible_bags(tab[i][0], tab)
                if rec:
                    for value in rec:
                        output.add(value)
    if len(output) > 0:
        return output
    else:
        return False


print(len(search_possible_bags('shiny gold', tab)))
