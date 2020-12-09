def find_first_invalid(tab, previous=25):
    for i in range(previous, len(tab)):
        valid = False
        for j in range(i-previous, i):
            for k in range(j, i):
                if tab[j] + tab[k] == tab[i] and tab[j] != tab[k]:
                    valid = True
        if not valid:
            return tab[i]