from seats import seat_coord, seat_id

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())
highest_id = 0


def search_empty_seat(id_tab):
    id_tab.sort()
    for i in range(0, len(id_tab)-1):
        if id_tab[i]+2 == id_tab[i+1]:
            return id_tab[i]+1



id_tab = []

for t in tab:
    row, column = seat_coord(t)
    id_tab.append(seat_id(row, column))

print(search_empty_seat(id_tab))
