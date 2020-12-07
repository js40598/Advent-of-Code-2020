from documents import extract_documents, check_fields

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
documents = extract_documents(tab)
counter = 0
for document in documents:
    if check_fields(document, required_fields):
        counter += 1
print(counter)
