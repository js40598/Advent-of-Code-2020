with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


for i in range(0, len(tab)):
    tab[i] = [tab[i][0], tab[i][1::]]


def rotate_waypoint(ship_position, waypoint_position, side, degree):
    relative_waypoint_position = [waypoint_position[0] - ship_position[0],
                                  waypoint_position[1] - ship_position[1]]
    if side == 'L':
        degree = -1 * degree
    while degree >= 360:
        degree += -360
    while degree < 0:
        degree += 360
    if degree == 90:
        relative_waypoint_position = [-relative_waypoint_position[1], relative_waypoint_position[0]]
    elif degree == 180:
        relative_waypoint_position = [-relative_waypoint_position[0], -relative_waypoint_position[1]]
    elif degree == 270:
        relative_waypoint_position = [relative_waypoint_position[1], -relative_waypoint_position[0]]
    return [ship_position[0] + relative_waypoint_position[0], ship_position[1] + relative_waypoint_position[1]]


def execute_command(command, ship_position, waypoint_position):
    directions = {
        'N': [1, 0],
        'E': [0, 1],
        'S': [-1, 0],
        'W': [0, -1],
    }
    if command[0] in 'NESW':
        waypoint_position = [waypoint_position[0] + directions[command[0]][0] * int(command[1]),
                             waypoint_position[1] + directions[command[0]][1] * int(command[1])]
    elif command[0] in 'LR':
        waypoint_position = rotate_waypoint(ship_position, waypoint_position, command[0], int(command[1]))
    elif command[0] in 'F':
        vector = [-ship_position[0] + waypoint_position[0], -ship_position[1] + waypoint_position[1]]
        ship_position = [ship_position[0] + vector[0] * int(command[1]),
                         ship_position[1] + vector[1] * int(command[1])]
        waypoint_position = [waypoint_position[0] + vector[0] * int(command[1]),
                             waypoint_position[1] + vector[1] * int(command[1])]
    return ship_position, waypoint_position


ship_position = [0, 0]
waypoint_position = [1, 10]
for command in tab:
    ship_position, waypoint_position = execute_command(command, ship_position, waypoint_position)
print(abs(ship_position[0]) + abs(ship_position[1]))
