def seat_coord(input):
    input = input.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
    return int(input[0:7], 2), int(input[7::], 2)


def seat_id(row, column):
    return row * 8 + column

