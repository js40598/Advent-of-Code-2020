with open('input.txt') as file:
    for line in file:
        if ',' in line:
            tab = (line.strip().split(','))

buses = []
for i in range(0, len(tab)):
    if tab[i] == 'x':
        pass
    else:
        buses.append([int(tab[i]), i])

buses = sorted(buses, key=lambda l:l[0], reverse=True)


def find_timestamp(buses, increment, timestamp=buses[0][0] - buses[0][1]):
    t = None
    while not t:
        i = 0
        try:
            while (timestamp + buses[i][1]) % buses[i][0] == 0:
                i += 1
        except IndexError:
            t = timestamp if timestamp != 304129 else None
        # timestamp += buses[0][0]
        timestamp += increment
    return t


increment = buses[0][0]
timestamp = buses[0][0] - buses[0][1]
for i in range(2, len(buses)+1):
    timestamp = find_timestamp(buses=buses[0:i], increment=increment, timestamp=timestamp)
    increment = increment * buses[i-1][0]
print(timestamp)
