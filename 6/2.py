with open('input.txt') as file:
    groups = []
    init = True
    for line in file:
        if init:
            groups.append([line.strip()])
            init = False
        else:
            if not line.strip():
                groups.append([])
            else:
                groups[-1].append(line.strip())

counter = 0
for group in groups:
    group_answers = {}
    for person in group:
        for answer in person:
            try:
                group_answers[answer] += 1
            except KeyError:
                group_answers[answer] = 1
    for key, value in group_answers.items():
        if value == len(group):
            counter += 1

print(counter)
