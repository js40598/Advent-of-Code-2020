from adjacents import get_vectors, fill_seats, empty_seats, count_occupied_seats

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(list(line.strip()))


new_tab = tab[::]
tab = []
while tab != new_tab:
    tab = new_tab[::]

    new_tab = fill_seats(tab, 'in_sight')

    new_tab = empty_seats(new_tab, 'in_sight')

print(count_occupied_seats(tab))





