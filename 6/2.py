from groups import extract_groups, correct_answers

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())

groups = extract_groups(tab)

counter = 0
for group in groups:
    counter += correct_answers(group)

print(counter)
