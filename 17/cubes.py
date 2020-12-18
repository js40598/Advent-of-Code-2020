def get_neighbor_coords(*args, neighbor):
    output = []
    for i in range(0, len(args)):
        output.append(args[i] + neighbor[i])
    return tuple(output)


def check_neighbor(*args, current_space):
    if len(args) == 1:
        args = args[0]
    length_space = current_space[::]
    for i in range(0, len(args)):
        if args[i] < 0 or args[i] >= len(length_space):
            return False
        length_space = length_space[0]
    cube = current_space[::]
    for i in range(0, len(args)):
        cube = cube[args[i]]
    if cube == '#':
        return True
    return False


def update_status(status, active_counter):
    if status == '#':
        if active_counter not in [2, 3]:
            return '.'
        else:
            return '#'
    elif status == '.':
        if active_counter == 3:
            return '#'
        else:
            return '.'


def count_active(current_space):
    total_active_counter = 0
    for value in current_space:
        if type(value) == str:
            if value == '#':
                total_active_counter += 1
        else:
            total_active_counter += count_active(value)
    return total_active_counter
