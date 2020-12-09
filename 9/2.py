with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(int(line.strip()))


for i in range(25, len(tab)):
    valid = False
    for j in range(i-25, i):
        for k in range(j, i):
            if tab[j] + tab[k] == tab[i] and tab[j] != tab[k]:
                valid = True
    if not valid:
        invalid = tab[i]

print(invalid)

for i in range(0, len(tab)):
    for j in range(i+1, len(tab)):
        if sum(tab[i:j+1]) == invalid:
            print(min(tab[i:j]) + max(tab[i:j]))
