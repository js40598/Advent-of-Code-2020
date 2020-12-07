def count_trees(tab, slope):
    width = len(tab[0])
    heigth = len(tab)
    counter = 0
    x = 0
    y = 0
    while y < heigth:
        if tab[y][x % width] == '#':
            counter += 1
        x += slope[1]
        y += slope[0]
    return counter