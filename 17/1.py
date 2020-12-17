import itertools

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())

for line in tab:
    print(line)

current_space = [[['.' for i in range(0, len(tab[0])+6*2)] for j in range(0, len(tab)+6*2)] for k in range(0, 1+6*2)]
input_z = int(len(current_space) / 2)
for i in range(0, len(tab)):
    for j in range(0, len(tab[0])):
        current_space[input_z][6+i][6+j] = tab[i][j]

for line in current_space[input_z]:
    print(line)

counter = 0
for neighbor in itertools.product([-1, 0, 1], repeat=3):
    if neighbor != (0, 0, 0):
        counter += 1
print(counter)

for _ in range(0, 6):
    new_space = [[['.' for i in range(0, len(tab[0])+6*2)] for j in range(0, len(tab)+6*2)] for k in range(0, 1+6*2)]
    for z in range(0, len(current_space)):
        for y in range(0, len(current_space[0])):
            for x in range(0, len(current_space[0][0])):
                active_counter = 0
                # print(z, y, x)
                for neighbor in itertools.product([-1, 0, 1], repeat=3):
                    neighbor_z = z + neighbor[0]
                    neighbor_y = y + neighbor[1]
                    neighbor_x = x + neighbor[2]
                    # print(neighbor_z, neighbor_y, neighbor_x)
                    check = True
                    if neighbor == (0, 0, 0):
                        check = False
                    if neighbor_z < 0 or neighbor_z >= len(current_space):
                        # print(neighbor_z)
                        check = False
                    if neighbor_y < 0 or neighbor_y >= len(current_space[0]):
                        check = False
                    if neighbor_x < 0 or neighbor_x >= len(current_space[0][0]):
                        check = False
                    if check:
                        # print('check')
                        if current_space[neighbor_z][neighbor_y][neighbor_x] == '#':
                            active_counter += 1
                    # else:
                    #     print(z, y, x)
                    # if active_counter > 0:
                    #     print(active_counter)
                if current_space[z][y][x] == '#':
                    # print('active', z, y, x, active_counter)
                    if active_counter not in [2, 3]:
                        new_space[z][y][x] = '.'
                        # print('active to inactive')
                    else:
                        new_space[z][y][x] = '#'
                elif current_space[z][y][x] == '.':
                    if active_counter == 3:
                        new_space[z][y][x] = '#'
                    else:
                        new_space[z][y][x] = '.'
                        # print('inactive to active')
    current_space = new_space[::][::][::]


# for line in current_space[input_z]:
#     print(line)

total_active_counter = 0
for z in range(0, len(current_space)):
    for y in range(0, len(current_space[0])):
        for x in range(0, len(current_space[0][0])):
            if current_space[z][y][x] == '#':
                total_active_counter += 1

print(total_active_counter)
