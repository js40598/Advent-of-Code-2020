from find_first_invalid import find_first_invalid

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(int(line.strip()))


print(find_first_invalid(tab))
