with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


for i in range(0, len(tab)):
    tab[i] = [tab[i][0], tab[i][1::]]
    print(tab[i])


def rotate(forward, side, degree):
    forwards = ['N', 'E', 'S', 'W']
    s = 1 if side == 'R' else -1
    current_degree = (forwards.index(forward)) * 90
    degree = degree * s + current_degree
    while degree >= 360:
        degree += -360
    while degree < 0:
        degree += 360
    return forwards[int(degree / 90)]


forward = 'E'
current_position = [0, 0]
directions = {
    'N': [1, 0],
    'E': [0, 1],
    'S': [-1, 0],
    'W': [0, -1],
}

for command in tab:
    if command[0] in 'NESW':
        current_position = [current_position[0] + directions[command[0]][0] * int(command[1]),
                            current_position[1] + directions[command[0]][1] * int(command[1])]
    elif command[0] in 'LR':
        forward = rotate(forward, command[0], int(command[1]))
    elif command[0] in 'F':
        current_position = [current_position[0] + directions[forward][0] * int(command[1]),
                            current_position[1] + directions[forward][1] * int(command[1])]
    else:
        print('sth')
print(current_position)
print(abs(current_position[0]) + abs(current_position[1]))
