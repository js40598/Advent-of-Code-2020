def validate_password(password):
    c = 0
    data = password.split(' ')
    data[0] = data[0].split('-')
    data[1] = data[1][0]
    try:
        if data[2][int(data[0][0]) - 1] == data[1] and data[2][int(data[0][1]) - 1] == data[1]:
            return False
        elif data[2][int(data[0][0]) - 1] == data[1] or data[2][int(data[0][1]) - 1] == data[1]:
            return True
    except IndexError:
        return False
    return False


with open('input.txt') as file:
    counter = 0
    for line in file:
        if validate_password(line.strip()):
            counter += 1


print(counter)
