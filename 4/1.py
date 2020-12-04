with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())
print(tab)
tab_sorted = ['']
for t in tab:
    if t == '':
        tab_sorted.append('')
    else:
        tab_sorted[-1] += ' {}'.format(t)

counter = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for p in tab_sorted:
    is_valid = True
    for required_field in required_fields:
        if required_field not in p:
            is_valid = False
    if is_valid:
        counter += 1
print(counter)