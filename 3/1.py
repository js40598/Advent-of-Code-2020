with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(list(line.strip()))

slope = [1, 3]

multiplier = 1 + len(tab)/len(tab[0]) * (slope[1] / slope[0])
multiplier = int(multiplier) + 1
for i in range(0, len(tab)):
    tab[i] = tab[i] * multiplier

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
    x += 3
    y += 1
print(counter)
