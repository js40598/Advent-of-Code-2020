with open('input.txt') as file:
    counter = 0
    for line in file:
        c = 0
        l = line.strip().split(' ')
        l[0] = l[0].split('-')
        l[1] = l[1][0]
        for letter in l[2]:
            if letter == l[1]:
                c += 1

        if c >= int(l[0][0]) and c <= int(l[0][1]):
            counter += 1

print(counter)
