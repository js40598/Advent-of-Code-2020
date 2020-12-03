with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(list(line.strip()))

slopes = [[1, 3],
          [1, 1],
          [1, 5],
          [1, 7],
          [2, 1]]

widthest_slope = 0

for slope in slopes:
    if slope[1] / slope[0] > widthest_slope:
        widthest_slope = slope[1] / slope[0]

multiplier = 1 + len(tab)/len(tab[0]) * widthest_slope
multiplier = int(multiplier) + 1
for i in range(0, len(tab)):
    tab[i] = tab[i] * multiplier

outputs = []
for slope in slopes:
    error = False
    x = 0
    y = 0
    counter = 0
    while not error:
        try:
            if tab[y][x] == '#':
                counter += 1
        except IndexError:
            error = True
        x += slope[1]
        y += slope[0]
    outputs.append(counter)

multiplied = 1
for output in outputs:
    multiplied = multiplied * output
print(outputs)
print(multiplied)
