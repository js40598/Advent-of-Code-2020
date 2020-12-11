with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(list(line.strip()))



def count_adjacent(tab, i, j):
    adjacent = 0
    # [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    if i == 0 and j == 0:
        vectors = [[1, 0], [0, 1], [1, 1]]
    elif i == 0 and j == len(tab[0]) - 1:
        vectors = [[0, -1], [1, -1], [1, 0]]
    elif i == len(tab) - 1 and j == 0:
        vectors = [[-1, 0], [-1, 0], [0, 1]]
    elif i == len(tab) - 1 and j == len(tab[0]) - 1:
        vectors = [[0, -1], [-1, -1], [-1, 0]]
    elif i == 0:
        vectors = [[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    elif i == len(tab) - 1:
        vectors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1]]
    elif j == 0:
        vectors = [[-1, 0], [-1, 1], [0, 1], [1, 0], [1, 1]]
    elif j == len(tab[0]) - 1:
        vectors = [[-1, 0], [-1, -1], [0, -1], [1, 0], [1, -1]]
    else:
        vectors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for vector in vectors:
        if tab[i+vector[0]][j+vector[1]] == '#':
            adjacent += 1


    # try:
    #     if tab[i-1][j-1] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    # try:
    #     if tab[i-1][j] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    # try:
    #     if tab[i-1][j+2] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    # try:
    #     if tab[i][j-1] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    # try:
    #     if tab[i][j+1] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    # try:
    #     if tab[i+1][j-1] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    # try:
    #     if tab[i+1][j] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    # try:
    #     if tab[i+1][j+1] == '#':
    #         adjacent += 1
    # except IndexError:
    #     pass
    return adjacent


new_tab = tab[::]
tab = []
while tab != new_tab:
    tab = new_tab[::]
    new_tab = [['.' for j in range(0, len(tab[0]))] for i in range(0, len(tab))]
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            if tab[i][j] == '#':
                new_tab[i][j] = '#'
                if count_adjacent(tab, i, j) >= 4:
                    new_tab[i][j] = 'L'
            elif tab[i][j] == 'L':
                new_tab[i][j] = 'L'

    tab = new_tab[::]


    new_tab = [['.' for j in range(0, len(tab[0]))] for i in range(0, len(tab))]
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            if tab[i][j] == 'L':
                if count_adjacent(tab, i, j) == 0:
                    new_tab[i][j] = '#'
                else:
                    new_tab[i][j] = 'L'
            elif tab[i][j] == '#':
                new_tab[i][j] = '#'



counter = 0
for i in range(0, len(tab)):
    for j in range(0, len(tab[0])):
        if tab[i][j] == '#':
            counter += 1

print(counter)



