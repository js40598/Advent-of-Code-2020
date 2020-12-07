from seats import seat_coord, seat_id

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())
highest_id = 0


id_tab = []

for t in tab:
    row, column = seat_coord(t)
    id_tab.append(seat_id(row, column))
print(max(id_tab))
