with open('input.txt') as file:
    counter = 0
    for line in file:
        c = 0
        data = line.strip().split(' ')
        data[0] = data[0].split('-')
        data[1] = data[1][0]
        try:
            if data[2][int(data[0][0]) - 1] == data[1] and data[2][int(data[0][1]) - 1] == data[1]:
                pass
            elif data[2][int(data[0][0]) - 1] == data[1] or data[2][int(data[0][1]) - 1] == data[1]:
                counter += 1
        except IndexError:
            pass

print(counter)
