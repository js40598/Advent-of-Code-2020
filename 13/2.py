import time
start_time = time.time()

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


def find_timestamp(buses, timestamp=buses[0][0] - buses[0][1], increment=None):
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


# max_id = 0
# for i in range(0, len(buses)):
#     if buses[i][0] > max_id:
#         max_id = buses[i][0]
#         max_id_index = i


t = None
# timestamp = int(100000000000000 / max_id) * max_id - max_id_index
timestamp = buses[0][0] - buses[0][1]
# timestamp = buses[0][0]
# while not t:
#     i = 0
#     try:
#         while (timestamp + buses[i][1]) % buses[i][0] == 0:
#             i += 1
#     except IndexError:
#         t = timestamp
#     # timestamp += buses[0][0]
#     timestamp += buses[0][0]
# print(t)


# increment = buses[0][0]
# for i in range(1, len(buses)):
#     increment = find_timestamp(buses[0:i], increment)
#     print(increment)

# increment = []
# for i in range(0, len(buses)-1):
#     increment.append(find_timestamp(buses[i:i+2], buses[0][0]))
#     buses.pop(0)
#     buses[i][1] = increment[-1]
# print(increment)


timestamp = find_timestamp(buses[0:4], increment=buses[0][0])
increment = buses[0][0] * buses[1][0] * buses[2][0] * buses[3][0]
print(timestamp)
# print(increment)
print(find_timestamp(buses, timestamp=timestamp, increment=increment))
print("--- %s seconds ---" % (time.time() - start_time))
#
# nwd = 'init'
# min_id = buses[0][0]
# while nwd:
#     nwd = []
#     for i in range(0, len(buses)):
#         if min_id > buses[i][0]:
#             min_id = buses[i][0]
#
#
