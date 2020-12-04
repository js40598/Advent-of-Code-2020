with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())
tab_sorted = [[]]
for t in tab:
    if t == '':
        tab_sorted.append('xxx:yyy')
    else:
        if t == tab[0]:
            tab_sorted[-1] += '{}'.format(t)
        else:
            tab_sorted[-1] += ' {}'.format(t)
for i in range(len(tab_sorted)):
    tab_sorted[i] = ''.join(tab_sorted[i])

counter = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for p in tab_sorted:
    fields_valid = True
    is_valid = True
    for required_field in required_fields:
        if required_field not in p:
            fields_valid = False
    if fields_valid:
        data = p.split(' ')
        print(data)
        id_dict = {d.split(':')[0]: d.split(':')[1] for d in data}
        if int(id_dict['byr']) > 1920 and int(id_dict['byr']) < 2002:
            pass
        else:
            is_valid = False
        if int(id_dict['iyr']) >= 2010 and int(id_dict['iyr']) <= 2020:
            pass
        else:
            is_valid = False
        if int(id_dict['eyr']) >= 2020 and int(id_dict['eyr']) <= 2030:
            pass
        else:
            is_valid = False
        if id_dict['hgt'][-2:-1] == 'cm':
            hgt = list(id_dict['hgt'])
            hgt.pop()
            hgt.pop()
            if int(hgt) > 150 and int(hgt) < 193:
                pass
            else:
                is_valid = False
        if id_dict['hgt'][-2:-1] == 'in':
            hgt = list(id_dict['hgt'])
            hgt.pop()
            hgt.pop()
            if int(hgt) > 59 and int(hgt) < 76:
                pass
            else:
                is_valid = False
        if id_dict['hcl'][0] == '#':
            for character in id_dict['hcl'][1:-1]:
                if character not in '0123456789abcdef':
                    is_valid = False
        else:
            is_valid = False
        if id_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            pass
        else:
            is_valid = False
        if len(id_dict['pid']) == 9:
            pass
        else:
            is_valid = False
        if is_valid:
            counter += 1
print(counter)
