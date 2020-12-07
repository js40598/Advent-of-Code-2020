from documents import extract_documents, check_fields

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def validate_document(document):
    if 1920 < int(document['byr']) < 2002:
        pass
    else:
        return False

    if 2010 <= int(document['iyr']) <= 2020:
        pass
    else:
        return False

    if 2020 <= int(document['eyr']) <= 2030:
        pass
    else:
        return False

    if document['hgt'][-2:-1] == 'cm':
        hgt = list(document['hgt'])
        hgt.pop()
        hgt.pop()
        if 150 < int(hgt) < 193:
            pass
        else:
            return False

    if document['hgt'][-2:-1] == 'in':
        hgt = list(document['hgt'])
        hgt.pop()
        hgt.pop()
        if 59 < int(hgt) < 76:
            pass
        else:
            return False

    if document['hcl'][0] == '#':
        for character in document['hcl'][1:-1]:
            if character not in '0123456789abcdef':
                return False
    else:
        return False

    if document['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        pass
    else:
        return False

    if len(document['pid']) == 9:
        pass
    else:
        return False

    return True


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
documents = extract_documents(tab)
counter = 0
for document in documents:
    if check_fields(document, required_fields):
        if validate_document(document):
            counter += 1
print(counter)
