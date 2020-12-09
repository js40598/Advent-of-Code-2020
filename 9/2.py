from find_first_invalid import find_first_invalid

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(int(line.strip()))


def find_contigous_set(tab, value):
    for i in range(0, len(tab)):
        contigous = [tab[i]]
        for j in range(i+1, len(tab)):
            contigous.append(tab[j])
            if sum(contigous) == value:
                return min(contigous) + max(contigous)


invalid = find_first_invalid(tab)

print(find_contigous_set(tab, invalid))
