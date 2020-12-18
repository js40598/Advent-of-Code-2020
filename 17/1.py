from cubes import get_neighbor_coords, check_neighbor, update_status, count_active
import itertools

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def generate_space(tab):
    return [[['.' for _ in range(0, len(tab[0])+6*2)] for _ in range(0, len(tab)+6*2)] for _ in range(0, 1+6*2)]


def insert_input(current_space, cycles):
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            current_space[cycles][cycles + i][cycles + j] = tab[i][j]
    return current_space


cycles = 6

current_space = generate_space(tab)

current_space = insert_input(current_space, cycles)

for _ in range(0, cycles):
    new_space = generate_space(tab)
    for z in range(0, len(current_space)):
        for y in range(0, len(current_space[0])):
            for x in range(0, len(current_space[0][0])):
                active_counter = 0
                for neighbor in itertools.product([-1, 0, 1], repeat=3):
                    if neighbor != (0, 0, 0):
                        if check_neighbor(get_neighbor_coords(z, y, x, neighbor=neighbor),
                                          current_space=current_space):
                            active_counter += 1
                new_space[z][y][x] = update_status(current_space[z][y][x], active_counter)
    current_space = new_space

print(count_active(current_space))
