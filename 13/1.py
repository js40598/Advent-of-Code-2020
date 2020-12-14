with open('input.txt') as file:
    for line in file:
        if ',' in line:
            tab = line.strip().split(',')
        else:
            timestamp = int(line.strip())

buses = []
for i in range(0, len(tab)):
    if tab[i] == 'x':
        pass
    else:
        buses.append(int(tab[i]))

output = sorted(buses, key=lambda l: timestamp % l, reverse=True)[0]
output = (output - timestamp % output) * output
print(output)
